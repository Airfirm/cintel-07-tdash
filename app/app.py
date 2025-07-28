# Import necessary libraries for the dashboard
import micropip
import plotly.express as px  # Replaced seaborn with plotly
from faicons import icon_svg
from shiny import reactive
from shiny.express import input, render, ui
from shinywidgets import render_plotly  # Added for Plotly support
import palmerpenguins
import plotly 

# Load penguins dataset into a DataFrame
df = palmerpenguins.load_penguins()

# Set dashboard page options with a title and fillable layout
ui.page_opts(title="Module 7 Penguins Dashboard - Femi", fillable=True)

# Create sidebar with filter controls and links
with ui.sidebar(title="Filter controls"):
    # Mass filter slider
    ui.input_slider("mass", "Mass", 2000, 6000, 6000)
    
    # Species filter checkbox group
    ui.input_checkbox_group(
        "species",
        "Species",
        ["Adelie", "Gentoo", "Chinstrap"],
        selected=["Adelie", "Gentoo", "Chinstrap"],
    )
    ui.hr()

    # Links section in sidebar
    ui.h6("Links")
    ui.a(
        "GitHub Source",
        href="https://github.com/Airfirm/cintel-07-tdash",
        target="_blank",
    )
    ui.a(
        "GitHub App",
        href="https://airfirm.github.io/cintel-07-tdash/",
        target="_blank",
    )
    ui.a(
        "GitHub Issues",
        href="https://github.com/Airfirm/cintel-07-tdash/issues",
        target="_blank",
    )
    ui.a("PyShiny", href="https://shiny.posit.co/py/", target="_blank")
    ui.a(
        "Template: Basic Dashboard",
        href="https://shiny.posit.co/py/templates/dashboard/",
        target="_blank",
    )
    ui.a(
        "See also",
        href="https://www.meetup.com/pymntos-twin-cities-python-user-group/",
        target="_blank",
    )

# Create value boxes showing penguin summary statistics
with ui.layout_column_wrap(fill=False):
    with ui.value_box(showcase=icon_svg("earlybirds")):
        "Number of penguins"
        @render.text
        def count():
            return filtered_df().shape[0]
        
    with ui.value_box(showcase=icon_svg("ruler-horizontal")):
        "Average bill length"
        @render.text
        def bill_length():
            return f"{filtered_df()['bill_length_mm'].mean():.1f} mm"
        
    with ui.value_box(showcase=icon_svg("ruler-vertical")):
        "Average bill depth"
        @render.text
        def bill_depth():
            return f"{filtered_df()['bill_depth_mm'].mean():.1f} mm"

# Main content area with two cards for visualizations and data display
with ui.layout_columns():
    # Card showing bill length vs depth scatter plot (now using Plotly)
    with ui.card(full_screen=True):
        ui.card_header("Bill length and depth")

        @render_plotly  # Changed to render_plotly for Plotly charts
        def length_depth():
            return px.scatter(
                data_frame=filtered_df(),
                x="bill_length_mm",
                y="bill_depth_mm",
                color="species",
                title="Bill Length vs. Depth by Species",
                labels={
                    "bill_length_mm": "Bill Length (mm)",
                    "bill_depth_mm": "Bill Depth (mm)",
                    "species": "Species"
                },
                hover_data=["species", "island", "body_mass_g"],
                template="plotly_white"
            ).update_traces(
                marker_size=10,
                marker_opacity=0.8,
                marker_line_width=1,
                marker_line_color="white"
            ).update_layout(
                legend_title_text="Species",
                hovermode="closest"
            )

    # Card showing penguin data grid
    with ui.card(full_screen=True):
        ui.card_header("Penguin Data")
        @render.data_frame
        def summary_statistics():
            cols = [
                "species",
                "island",
                "bill_length_mm",
                "bill_depth_mm",
                "body_mass_g",
            ]
            return render.DataGrid(filtered_df()[cols], filters=True)

# Reactive calculation to filter the DataFrame based on user input
@reactive.calc
def filtered_df():
    filt_df = df[df["species"].isin(input.species())]
    filt_df = filt_df.loc[filt_df["body_mass_g"] < input.mass()]
    return filt_df