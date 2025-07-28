# Import necessary libraries for the dashboard
import seaborn as sns
from faicons import icon_svg # For Font Awesome icons, using icons in the dashboard
from shiny import reactive # For reactive programming
from shiny.express import input, render, ui # Shiny UI components
import palmerpenguins # Penguins dataset

# Load penguins dataset into a DataFrame
df = palmerpenguins.load_penguins()

# Set dashboard page options with a title and fillable layout
ui.page_opts(title="Module 7 Penguins Dashboard - Femi", fillable=True)

# Create sidebar with filter controls and links
with ui.sidebar(title="Filter controls"):
    # Mass filter slider
    
    # Species filter checkbox group
    ui.input_checkbox_group(
        "species",
        "Species",
        ["Adelie", "Gentoo", "Chinstrap"],
        selected=["Adelie", "Gentoo", "Chinstrap"],
    )
    ui.hr() # Horizontal rule for visual separation

    # Links section in sidebar
    ui.h6("Links")
    ui.a(
        "GitHub Source",
        href="https://github.com/denisecase/cintel-07-tdash",
        target="_blank",
    )
    ui.a(
        "GitHub App",
        href="https://denisecase.github.io/cintel-07-tdash/",
        target="_blank",
    )
    ui.a(
        "GitHub Issues",
        href="https://github.com/denisecase/cintel-07-tdash/issues",
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
        href="https://github.com/denisecase/pyshiny-penguins-dashboard-express",
        target="_blank",
    )

# Create value boxes showing penguin summary statistics
with ui.layout_column_wrap(fill=False):

    # Value box showing number of penguins
    with ui.value_box(showcase=icon_svg("earlybirds")):
        "Number of penguins"

        @render.text
        def count():
            return filtered_df().shape[0] # Number of rows in filtered DataFrame
        
    # Value box showing average bill length
    with ui.value_box(showcase=icon_svg("ruler-horizontal")):
        "Average bill length"

        @render.text
        def bill_length():
            return f"{filtered_df()['bill_length_mm'].mean():.1f} mm" # Calculate mean bill length
        
    # Value box showing average bill depth
    with ui.value_box(showcase=icon_svg("ruler-vertical")):
        "Average bill depth"

        @render.text
        def bill_depth():
            return f"{filtered_df()['bill_depth_mm'].mean():.1f} mm" # Calculate mean bill depth

# Main content area with two cards for visualizations and data display
with ui.layout_columns():

    # Card showing bill length vs depth scatter plot
    with ui.card(full_screen=True):
        ui.card_header("Bill length and depth")

        @render.plot
        def length_depth():
            return sns.scatterplot( # Create scatter plot
                data=filtered_df(),
                x="bill_length_mm",
                y="bill_depth_mm",
                hue="species", # Color by species
            )

    # Card showing penguin data grid
    with ui.card(full_screen=True):
        ui.card_header("Penguin Data")

        @render.data_frame
        def summary_statistics():
            cols = [ # Columns to display in the data grid
                "species",
                "island",
                "bill_length_mm",
                "bill_depth_mm",
                "body_mass_g",
            ]
            return render.DataGrid(filtered_df()[cols], filters=True) # Interactive data grid


#ui.include_css(app_dir / "styles.css")

# Reactive calculation to filter the DataFrame based on user input
@reactive.calc
def filtered_df():
    filt_df = df[df["species"].isin(input.species())]
    filt_df = filt_df.loc[filt_df["body_mass_g"] < input.mass()]
    return filt_df
