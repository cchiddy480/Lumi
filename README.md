# Lumi

**Lumi** is an open-source, drag-and-drop UI builder specifically designed to make Python application development accessible for kids, teenagers, and beginners. Lumi combines the simplicity of visual programming with the power of Python code generation, enabling users to learn both visual and textual coding seamlessly.

## Key Features
- **Drag-and-Drop Editor**: Create user interfaces with an intuitive drag-and-drop editor, similar to visual tools like Scratch, but with real Python application power.
- **Code Generation**: Real-time Python code generation that reflects what users build visually, offering insights into how UI elements translate into code.
- **Educational Focus**: Built with the educational context in mind, Lumi is streamlined for use in schools and by young learners. It’s designed to be simple, fun, and informative.
- **Cross-Platform Compatibility**: Lumi is compatible with Windows, macOS, and Linux, making it easy to use in diverse environments.

## Getting Started
### Prerequisites
- **Python 3.7+**: Ensure Python is installed on your machine. You can download it from [Python's official website](https://www.python.org/downloads/).
- **Dependencies**: Lumi relies on PyQt5 for the drag-and-drop interface. Install the necessary dependencies by running the command:
  ```sh
  pip install -r requirements.txt
  ```

### Core Dependencies for Lumi
- **PyQt5** - Main library for GUI creation and drag-and-drop functionality
  ```
  PyQt5==5.15.9
  ```
- **PyInstaller** - To package the application into executable formats
  ```
  PyInstaller==5.13.0
  ```
- **Additional tools for code generation and support** (as needed later)
  - Any other dependencies will be added as the project evolves

### Installation
1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/Lumi.git
   cd Lumi
   ```
2. **Install Dependencies**
   Run the following command to install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```

### Running Lumi
To start Lumi, run the following command:
```sh
python src/main.py
```
This will open the Lumi main window, where you can begin experimenting with the drag-and-drop interface.

## Directory Structure
```
Lumi/
├── src/                  # Main source code
│   ├── main.py           # Entry point for Lumi
│   ├── ui_manager.py     # Manages UI elements
│   ├── drag_and_drop/    # Components for drag-and-drop editor
│   ├── code_generator/   # Handles generating code from UI actions
│   ├── components/       # Custom components (buttons, labels, etc.)
│   └── utils/            # Utility functions
├── docs/                 # Documentation
│   ├── setup_guide.md    # Setup instructions
│   ├── user_manual.md    # User manual for end users
│   └── developer_guide.md# Guide for developers wanting to contribute
├── examples/             # Example projects
│   ├── sample_app1/      # Example showcasing basic UI components
│   └── sample_app2/      # More advanced example
├── tests/                # Unit and integration tests
├── README.md             # Overview of the project
└── requirements.txt      # Dependencies required for Lumi
```

## Contributing
Contributions are welcome! Whether you are a developer, teacher, or student, there are many ways you can contribute to Lumi:
- **Report Bugs**: If you encounter any bugs, please report them using the GitHub Issues page.
- **Suggest Features**: We are always looking for new ideas to make Lumi better.
- **Submit Pull Requests**: If you are a developer, feel free to fork the repository, make your changes, and submit a pull request.

### How to Contribute
1. **Fork the Repository** on GitHub.
2. **Clone Your Fork** locally:
   ```sh
   git clone https://github.com/yourusername/Lumi.git
   ```
3. **Create a Branch** for your feature or bug fix:
   ```sh
   git checkout -b feature-branch-name
   ```
4. **Make Your Changes** and commit them:
   ```sh
   git add .
   git commit -m "Add a descriptive commit message"
   ```
5. **Push to Your Fork** and submit a pull request:
   ```sh
   git push origin feature-branch-name
   ```

## License
Lumi is licensed under the MIT License. See `LICENSE` for more information.

## Contact
For any questions, suggestions, or feedback, feel free to open an issue or reach out via the GitHub repository.

Happy coding with Lumi!

