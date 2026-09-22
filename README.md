# Moodnest

Moodnest is a web application for mental well-being and mindfulness. The application helps users track their daily moods, complete guided breathing exercises, and find mental health resources.

## Project Pages

The project contains four main pages:

### Home (index.html)
The home page is the main landing page of the application.
- It introduces the website purpose and core features.
- It provides top navigation links to all sections.
- It contains quick-action buttons to navigate directly to each feature: take a breath, track your mood, and find some help.

### Relax (breath.html)
The relax page provides an interactive breathing exercise tool.
- Users start a guided session with the session control button.
- An animated visual guide indicates inhale and exhale intervals.
- A voice control button enables or disables spoken audio instructions for accessibility.

### Daily Mood Log (moodLog.html)
The daily mood log page records user feelings and daily reflections.
- Users select an icon that represents their current mood state.
- Users select tags for factors that influence their mood, such as work, sleep, friends, or health.
- A text area allows users to write personal reflections.
- A microphone button provides speech-to-text live transcription through the Web Speech API.

### Resource Hub (resources.html)
The resource hub lists curated mental health support services.
- Resources are grouped into four categories: Articles, Apps, Crisis Support, and Community.
- Category buttons filter the displayed resource cards in real time.
- A submission form allows users to suggest new support resources.

## Deployment and Execution

### GitHub Pages (Static Hosting)
The application runs as a static website directly from the repository root.
1. Open the repository on GitHub.
2. Navigate to **Settings** and select **Pages**.
3. Under **Build and deployment**, set **Source** to `Deploy from a branch`.
4. Select the `main` branch and the `/ (root)` folder.
5. Click **Save**.

### Local Static Execution
1. Clone the repository:
   ```bash
   git clone https://github.com/austinmusebe/HCIProject.git
   ```
2. Open `index.html` in any standard web browser.

### Flask Backend Execution (Optional)
The `flask_resources` folder contains an alternative implementation that uses Python Flask and SQLite.
1. Create a Python virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - Windows Command Prompt:
     ```cmd
     venv\Scripts\activate.bat
     ```
   - Windows PowerShell:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - macOS / Linux:
     ```bash
     source venv/bin/activate
     ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the application:
   ```bash
   cd flask_resources
   python app.py
   ```
5. Open `http://127.0.0.1:5000` in your web browser.
