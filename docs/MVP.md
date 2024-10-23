# Lumi - Minimum Viable Product (MVP)

### Project Overview
Lumi is an open-source, user-friendly development framework designed to make app and UI creation accessible to children, teenagers, and educators. It aims to provide an intuitive drag-and-drop interface for creating applications, paired with the ability to view and learn from the underlying code. Lumi is specifically tailored for educational environments, focusing on ease of installation, cross-platform compatibility, and an engaging user experience.

### Core Features

1. **Drag-and-Drop UI Editor**
   - A visual editor where users can drag and drop various UI components (buttons, text boxes, labels, images) into a canvas to create a layout.
   - Components should be intuitively organized in a toolbox, allowing users to easily find and use different elements.
   - Users should be able to arrange, resize, and modify component properties using a straightforward, interactive interface.

2. **Two-Way Code Generation**
   - Lumi will generate Python code that corresponds to the components and layout users create in the drag-and-drop editor.
   - Users should have the ability to switch between the visual interface and a code editor, allowing them to make modifications to the code directly.
   - Changes made in the code editor should be reflected in the visual editor and vice versa, providing a seamless transition between both modes.

3. **Beginner-Friendly Interface**
   - The user interface must be highly intuitive, with minimal configuration steps, large and recognizable icons, and clear labeling.
   - Pre-built templates should be included for common applications such as simple games, to-do lists, or calculator apps.
   - Tooltips and hints should be incorporated to guide users as they work, ensuring the learning process is smooth and frustration-free.

4. **Easy Installation for Schools**
   - Lumi must be easy to install across multiple devices with minimal intervention. This includes creating a streamlined installer for IT teams.
   - A portable version of Lumi should be made available, allowing it to be run without needing full system installation or administrative privileges.
   - Cross-platform support for Windows, macOS, and Linux, ensuring it can be used regardless of the hardware available in schools.

5. **Example Projects & Templates**
   - Lumi will include built-in templates and example projects to kickstart users' creativity and provide an introduction to its features.
   - Projects such as a "Clicker Game," "Interactive Quiz," and "Simple Drawing App" will be available for users to modify and explore.

### Technical Requirements

- **Language**: The backend logic will be built using Python, ensuring readability and ease of learning for newcomers.
- **Frontend Framework**: Use **PyQt** or **Electron** to develop the drag-and-drop interface, focusing on accessibility and ease of use.
- **Packaging Tools**: Use **PyInstaller** or an equivalent to create executable files for Windows, macOS, and Linux, making the deployment as smooth as possible.

### Success Criteria for MVP

1. **Drag-and-Drop Editor**: Users can successfully create a basic UI layout using a visual drag-and-drop interface.
2. **Two-Way Code Sync**: Users can modify their design visually or in the code editor, with both interfaces staying in sync.
3. **Beginner Templates**: Include at least three pre-built templates (e.g., calculator, to-do list, simple game).
4. **Installation Simplicity**: Lumi should be installable with a single installer and run on multiple platforms without complicated setup.
5. **Positive User Feedback**: Initial user testing with a small group of educators and students should show positive feedback, focusing on ease of use, engagement, and educational value.

### Next Steps
- **Research & Prototyping**: Research the tools required to create the drag-and-drop interface and prototype the basic functionality.
- **Set Up Development Environment**: Establish the GitHub repository, set up continuous integration (CI), and define development guidelines.
- **Community Involvement**: Begin reaching out to potential contributors to help with the project, such as educators and developers.

Lumi's MVP will serve as a starting point to transform how young people interact with and learn about software development. By keeping it visual, intuitive, and educational, Lumi aims to make coding fun, accessible, and impactful for the next generation.

