# `garcialab.berkeley.edu`

Welcome to the GitHub Repository for the Garcia Lab website!


## Directory Structure
This repository obviously has a lot of directories and files, but you don't have 
to touch most of them to add/remove content to the website. Below is a brief outline 
of what all the directories/subdirectories are and when/if you would need to 
edit their contents. 

### `_data`: Where most of the site content lives
The `_data` folder contains an array of `YAML` files which define the content of 
the website. 

* `index.yml`: This defines what the boxes are on the front page, where they link to, and what images they show. 
* `nav.yml` : This defines the navigation links shown on the top of every page 
of the website and where they link to. 
* `members.yml` : This defines all of the *current* members of the lab. The data in this file is what populates the "people" page of the website. **Edit this file to add/remove members from the lab.**
* `former_members.yml` : THis defines all of the former members of the lab, including all of the visitors. 

# 📌 Making Edits
Only **approved administrators** can commit directly to the `master` branch. All other contributors must follow these steps to make changes.

### **1️⃣ Create a New Branch**
Before making any changes, create a branch:
```sh
git checkout -b your-branch-name
```
Push it to GitHub:
```sh
git push origin your-branch-name
```

### **2️⃣ Make Your Edits and Commit**
Modify the necessary files, then commit your changes:
```sh
git add .
git commit -m "Description of changes"
git push origin your-branch-name
```

### **3️⃣ Create a Pull Request (PR)**
After pushing your changes, go to **GitHub → Pull Requests → New PR**, then:
- Select `master` as the **base branch**.
- Select your branch as the **compare branch**.
- Click **"Create Pull Request"**.

### **4️⃣ Get Approval**
Your PR must be reviewed and approved by **one of the maintainers** before it can be merged. In your PR, make sure you include the following:
- **[Your Name]**
- **[Description of the changes made]**

A PR **cannot be merged** until at least one admin has reviewed and approved it.

### **5️⃣ Merge the PR**
Once approved, you can merge the PR into `master`:
```sh
git checkout master
git pull origin master
git merge your-branch-name
git push origin master
```

---

## 🔒 **Branch Protection Rules**
To maintain the integrity of the website:
- 🚫 **Direct commits to `master` are blocked** except for approved maintainers.
- ✅ **All changes must go through a PR and be approved before merging.**
- 🛠️ **PR previews are automatically deployed** for testing before merging.

---

## 📬 **Need Help?**
If you run into issues, open a GitHub **Issue** or reach out to one of the maintainers.
