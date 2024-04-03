from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Zyquier_Resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Zyquier Brownridge"
PAGE_ICON = ":wave:"
NAME = "Zyquier"
DESCRIPTION = """
Solution-oriented and problem solver with 3 years of experience in Cyber Security while using software development skills for solving complex problems as well. Highly skilled in communication, collaboration, and technical documentation.
"""

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/zy24/",
    "GitHub": "https://github.com/Zyquier",
}
PROJECTS = {
    "🏆 Machine Learning -CYBER IDS SYSTEM": "https://github.com/Zyquier/CYBER/tree/main/ml_ids",
    "🏆 PORT SCANNER - CYBER PORT SCANNER THAT SAVE DETAILS IN EXCEL": "https://github.com/Zyquier/CYBER",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 4
st.write('\n')
st.write("🎯", "**Security Engineer Consultant | CDW**")
st.write("01/2024 - present")
st.write(
    """
- ►Strategize and assist in the development of IAM solutions
- ►Establishes trust with the customers in order to becomes a trusted advisor clients for IAM-related services.
- ►Deploying SailPoint IIQ and adding users following full Identity Life cycle management provision plan.
"""
)

# --- JOB 1
st.write("🏴‍☠️", "**Security Engineer(TA) | TIAA**")
st.write("01/2022 - 1-2024")
st.write(
    """

🎩🎩🎩🎩
 4th Rotation: IAMOps(PamUnix Team):
- ►600 Users bulk add to Highly privilege accounts using PowerShell scripting
- ►Created Splunk report to notify the team of Service accounts that were still in active/inactive every 30 days
- ►Managing users on standard(UNIX) and privileged hosts(PAM) from service now requests tickets. 
- ►Processing RBAC users for each group they are assigned to and from Active Directory or CyberArk. 
- ►Developed Python Script to automate UNIX TERMINATIONS. 

🚧🚧🚧
 3rd Rotation: SecOps(Security Operations/Security Logging):
- ►Docker Container + Linux and Python.
- ►Created Splunk dashboards to visualize and analyze security data effectively.
- ►Implemented SPL searches to extract relevant information from the Splunk platform.
- ►Fine-tuned existing use cases and searches to improve their efficiency and accuracy.
- ►Merged existing dashboards to consolidate information and provide a comprehensive view of the security landscape.
- ►Configured Splunk alerts, reports, and saved searches to proactively monitor and detect security incidents.
- ►Gained knowledge of the collaboration between the Detective Team and Response Team within the Security Operations Center (SOC).
- ►Utilized CI/CD (Continuous Integration/Continuous Deployment) practices for managing and deploying Splunk use cases using Linux and tools like PuTTY.
- ►Employed Linux for deploying Splunk use cases.
- ►Collaborated and communicated with various teams to troubleshoot and resolve issues within the Splunk infrastructure.
- ►Utilized Python in conjunction with Splunk for automation tasks.
- ►Participated in Kanban Agile Standup Daily meetings to facilitate efficient project management and communication.

🏋️‍♂️🏋️‍♂️
2nd Rotation: Data Loss Prevention (DLP):
- ►Utilized the Symantec Endpoint Protection Tool for data loss prevention activities.
- ►Focused on Data in Motion (DIM), specifically monitoring data transfers such as emails.
- ►Analyzed both internal and external users, paying attention to specific domain names.
- ►Concentrated efforts on identifying and preventing the unauthorized transmission of classified data from internal users.
- ►Acquired knowledge about DLP policies and their purpose.
- ►Learned how policies are configured and the specific rules and detections they employ.
- ►Developed a scripting tool using Python to automate certain DLP tasks.
- ►Created automation scripts in Python to streamline and enhance DLP processes.
- ►Worked with the Symantec REST API using Python to interact with DLP functionalities.

🎱
- ►1st Rotation - Application Security Vulnerability Management:
- ►Analyzed weekly vulnerabilities, both internal and external scans, using Tableau dashboards.
- ►Utilized the Remediation Dashboard in Tableau to compare and validate upcoming tasks for the next week and current month. This information was then organized within an Excel file.
- ►Managed metrics for top vulnerabilities, categorizing them as Medium, High, or Very High. Also tracked the number of applications without scans, both for internet-facing and internal applications.
- ►Automated controls by leveraging Python scripting.
- ►Utilized Python to interact with the Veracode REST API for in-scope applications. Extracted relevant data from the API responses in JSON format and processed it for validation purposes and automation. This involved generating Excel files to store the data.
"""
)

# --- JOB 2
st.write('\n')
st.write("🎯", "**Cloud Security Intern | Lenovo**")
st.write("05/2021 - 10/2021")
st.write(
    """
- ►Conducted Vulnerability Analysis to identify potential security weaknesses.
- ►Acquired proficiency in various penetration testing tools, including Burp Suite.
- ►Utilized Jira to discover security findings and conduct security reviews.
- ►Created a dashboard in Jira to track and manage Vulnerability Findings.
- ►Demonstrated proficiency in cloud technologies, specifically Azure.
- ►Familiarity with the OSI model for network communication.
- ►In-depth understanding of HTTP/HTTPS protocols.
- ►Knowledgeable about different types of vulnerabilities and their mitigation strategies.
"""
)

# --- JOB 3
st.write('\n')
st.write("⚓", "**Software Engineer Intern | Science Gateways Community Institute**")
st.write("05/2020 - 10/2020")
st.write(
    """
- ►Completed certifications in High-Performance Computing using Python and Responsible Conduct of ----Research Investigators and Key Personnel at a competitive coding institute.
- ►Proficient in HTML web development.
- ►Acquired knowledge and hands-on experience with science gateways such as Apache Airavata, Hub Zero, and Tapis.
- ►Actively participated in PEARC20 and PEARC20 Hackathon.
- ►Engaged in cross-functional team-building activities.
- ►Enhanced proficiency in JavaScript and HTML coding.
- ►Familiarity with Agile Development methodologies.
- ►Proficient in MySQL.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
