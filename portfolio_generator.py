import os
import shutil

# User input
def get_user_input():
    print("Welcome to the Portfolio Website Generator!")
    name = input("Enter your name: ")
    bio = input("Write a short bio about yourself: ")
    contact_email = input("Enter your contact email: ")
    github_link = input("Enter your GitHub profile link: ")
    linkedin_link = input("Enter your LinkedIn profile link: ")
    projects = []
    print("Add your projects (type 'done' to finish):")
    while True:
        project = input("> ")
        if project.lower() == "done":
            break
        projects.append(project)
    return {
        "name": name,
        "bio": bio,
        "contact_email": contact_email,
        "github_link": github_link,
        "linkedin_link": linkedin_link,
        "projects": projects,
    }

# Generate HTML file
def generate_html(data):
    # Get the absolute path of the script's directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(base_dir, "templates", "index.html")
    css_path = os.path.join(base_dir, "templates", "style.css")
    output_dir = os.path.join(base_dir, "output")

    # Read the template HTML
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template HTML not found: {template_path}")

    with open(template_path, "r") as template_file:
        template = template_file.read()

    # Replace placeholders with user input
    html_content = template.format(
        name=data["name"],
        bio=data["bio"],
        contact_email=data["contact_email"],
        github_link=data["github_link"],
        linkedin_link=data["linkedin_link"],
        projects="".join([f"<li><a href='{project}' target='_blank'>{project}</a></li>" for project in data["projects"]]),
    )


    # Save the generated HTML to the output folder
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(os.path.join(output_dir, "index.html"), "w") as output_file:
        output_file.write(html_content)

    # Copy CSS file to output folder
    if os.path.exists(css_path):
        shutil.copy(css_path, os.path.join(output_dir, "style.css"))
    else:
        print(f"Warning: CSS file not found: {css_path}")

    print(f"Portfolio website generated! Open '{os.path.join(output_dir, 'index.html')}' in your browser.")

# Main function
if __name__ == "__main__":
    print("Current working directory:", os.getcwd())
    print("Looking for templates/index.html...")

    user_data = get_user_input()
    generate_html(user_data)
