

# Project Setup and Contribution Guide

This document explains how to clone the repository, set up the development environment, install required dependencies, and create a working branch.

---

## 1. Cloning the Repository

First, clone the repository from GitHub to your local machine:

```bash
git clone https://github.com/Daniel-Chacha/wave_reveal.git
```

Navigate into the project directory:

```bash
cd wave_reveal
```

---

## 2.   Create and Activate a Virtual Environment

Using a virtual environment helps isolate project dependencies.

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Linux / macOS**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

---

## 3. Install Project Dependencies

All required Python packages are listed in the `requirements.txt` file.

Install them using:

```bash
pip install -r requirements.txt
```

---

## 4. Main Libraries and Modules Used

The project relies on the following core Python libraries:

### • NumPy

Used for numerical computing and handling multi-dimensional arrays.

### • Pandas

Provides data structures and tools for data manipulation and analysis.

### • Matplotlib

Used for creating static, animated, and interactive visualizations.

### • Seaborn

Built on top of Matplotlib; provides high-level statistical data visualization.

### • TensorFlow

Used for building and training machine learning and deep learning models.

### • Jupyter Notebook

Provides an interactive environment for running and documenting experiments.

### • IPykernel

Enables the project’s virtual environment to be selectable as a kernel inside Jupyter Notebooks.

---

## 5.Creating and Using a Feature Branch

Before making changes, create a new branch:

```bash
git checkout -b <branch-name>
```

Example:

```bash
git checkout -b daniel
```

Verify your current branch:

```bash
git branch
```

---



## 6.  Getting started with Jupyter Notebook 

Install "Jupyter" extension by Microsoft.
Then you can create jupyter notebook files normally on vs code as you do with other files but the filename ends with .ipynb
After creating  a file click **Kernel → Change Kernel → Python (venv)...Recommended**.
You are now good to go.
Create cells to write your code .
---

## 7. Pushing Your Branch to the Remote Repository

After making changes and committing them:

```bash
git push origin <branch-name>
```

---

## 8. Additional Notes

* Always pull the latest changes from the main branch before starting new work:

  ```bash
  git pull origin main
  ```
* Keep commits small and descriptive.
* Ensure notebooks run without errors before pushing changes.

---

**Happy Codding!**
