# cintel-07-tdash

# PyShiny Basic Dashboard (Penguins)

---

# 🐧 Penguins Dashboard – Module 7

A PyShiny-based interactive dashboard that visualizes and analyzes the **Palmer Penguins dataset**. This application allows users to filter penguins by species and mass, view summary statistics, and explore visualizations with a responsive UI powered by [PyShiny](https://shiny.posit.co/py/).

## 📊 Features

* Interactive **checkbox filter** for penguin species (Adelie, Gentoo, Chinstrap)
* Mass filtering using a slider (editable if uncommented)
* Value boxes displaying:

  * Total number of penguins (after filtering)
  * Average bill length
  * Average bill depth
* Seaborn-based **scatterplot** showing bill length vs. bill depth, color-coded by species
* Interactive **data grid** of penguin metrics (island, bill, mass)
* External resource links in the sidebar for documentation and reference

## 🚀 Getting Started

### 🔧 Installation

1. Clone this repository:

```bash
git clone https://github.com/Airfirm/cintel-07-tdash.git
cd cintel-07-tdash
```

2. Install dependencies:

```bash
pip install shiny faicons palmerpenguins seaborn
```

> Optionally, use a `requirements.txt` file if you prefer pinned versions.

### ▶️ Run the App

```bash
shiny run --reload app.py
```

The app will be available at `http://localhost:8000`.

## 📁 File Structure

```
.
├── app.py            # Main PyShiny dashboard application
├── README.md         # Project documentation
└── requirements.txt  # Optional: list of dependencies
```

## 🔗 Useful Links

* [GitHub Source](https://github.com/Airfirm/cintel-07-tdash)
* [Live App](https://airfirm.github.io/cintel-07-tdash/)
* [File Issues](https://github.com/Airfirm/cintel-07-tdash/issues)
* [PyShiny Documentation](https://shiny.posit.co/py/)
* [Basic Dashboard Template](https://shiny.posit.co/py/templates/dashboard/)
* [Python Meetups - PyMNtos](https://www.meetup.com/pymntos-twin-cities-python-user-group/)

## 📦 Dependencies

* `shiny`
* `faicons`
* `palmerpenguins`
* `seaborn`
* `shinylive`
* `seaborn`
* `pandas`
* `plotly`
* `shinywidgets`
* `plotly.express`

Install them all using:

```bash
pip install shiny faicons palmerpenguins seaborn
```

---


## Project Communication Starts with README.md
The README.md file introduces our project. It's the first file visitors see and a well-crafted README is engaging and useful, providing an overview, and concise instructions.

An effective README.md helps others - but us too, when we return after several months. Generally recommended features include:

Project Title 
Project Description or Introduction
Installation Requirements and Commands - List of prerequisites and step-by-step instructions for setting up the project
Commands to Build and/or Run the App
Optional Screenshots or GIFs - show the application in action, offering a preview of the functionality.
Clickable Links to Resources - acknowledges our resources and offer additional information, such as links to documentation, APIs, or related projects.

## Tools

- Python
- Shiny for Python
- VS Code + Python Extension
- Git
- GitHub

## Try in the Browser

Go to PyShiny Templates at <https://shiny.posit.co/py/templates/>.
Go to Dashboards / Basic Dashboard.

- <https://shiny.posit.co/py/templates/dashboard/>

## Reference App with Detailed Instructions

For more detailed instructions, see <https://github.com/denisecase/pyshiny-penguins-dashboard-express>.
That project README.md has more detailed instructions, including reminders for Mac and Linux. 

## Get the Code

Fork this project into your own GitHub account.
Clone **your** GitHub repo down to your local machine.
IMPORTANT: Use your GitHub **username** in place of denisecase.
[GitHub CLI](https://cli.github.com/) may work better on some machines.

```shell
git clone https://github.com/denisecase/cintel-07-tdash
```

## Run Locally - Initial Start

After cloning your project down to your Documents folder, open the project folder for editing in VS Code.

Create a local project virtual environment named .venv, activate it, and install the requirements.

When VS Code asks to use it for the workspace, select Yes.
If you miss the window, after installing, select from the VS Code menu, View / Command Palette, and type "Python: Select Interpreter" and select the .venv folder.

Open a terminal (VS Code menu "View" / "Terminal") in the root project folder and run these commands (for Windows - the activate command is slightly different Linux/Mac).

```shell
py -m venv .venv
.venv\Scripts\Activate
py -m pip install --upgrade pip setuptools
py -m pip install --upgrade -r requirements.txt
```

Open a terminal (VS Code menu "View" / "Terminal") in the root project folder and run these commands.

```shell
shiny run --reload --launch-browser app/app.py
```

Open a browser to <http://127.0.0.1:8000/> and test the app.

## Run Locally - Subsequent Starts

Open a terminal (VS Code menu "View" / "Terminal") in the root project folder and run these commands.

```shell
.venv\Scripts\Activate
shiny run --reload --launch-browser app/app.py
```

While the app is running, the terminal is fully engaged and cannot be used for other commands. 
To kill the terminal, click the trashcan icon in the VS Code terminal window. 

## After Changes, Export to Docs Folder

Export to docs folder and test GitHub Pages locally.

Open a new terminal (VS Code menu "Terminal" / "New Terminal") in the root project folder and run these commands. 
Remember to activate the environment first. 

```shell
.venv\Scripts\Activate
shiny static-assets remove
shinylive export app docs
py -m http.server --directory docs --bind localhost 8008
```

Open a browser to <http://[::1]:8008/> and test the Pages app.

## Push Changes back to GitHub

Open a terminal (VS Code menu "Terminal" / "New Terminal") in the root project folder and run these commands.

```shell
git add .
git commit -m "Useful commit message"
git push -u origin main
```

## Enable GitHub Pages

Go to your GitHub repo settings and enable GitHub Pages for the docs folder.

