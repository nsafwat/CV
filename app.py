from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Nour El-Din Safwat"
PAGE_ICON = ":wave:"
NAME = "Nour El-Din Safwat"
DESCRIPTION = """Avionics Engineer, Ph.D."""
EMAIL = "eng.nours@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/nsafwat/",
    "Researchgate": "https://www.researchgate.net/profile/Nour-El-Din-Safwat",
    "Web of Science": "https://www.webofscience.com/wos/author/record/2266663",
}
Publications = {
    "🏆 2022 Safwat, Nour El-Din, I. M. Hafez, and Fatma Newagy. 'UGPL: A MATLAB application for UAV-to-Ground path loss calculations.' Software Impacts 12 (2022): 100277": "https://www.sciencedirect.com/science/article/pii/S2665963822000306",
    "🏆 2022 Safwat, Nour El-Din, Ismail Mohammed Hafez, and Fatma Newagy. '3D placement of a new tethered UAV to UAV relay system for coverage maximization.' Electronics 11.3 (2022): 385.": "https://www.mdpi.com/2079-9292/11/3/385/htm",
    "🏆 2021 Safwat, Nour El-Din, Ismail M. Hafez, and Fatma Newagy. 'Air-To-Air Channel Model For UAVs In Dense Urban Environments.'2021 5th International Conference on Electrical, Electronics, Communication, Computer Technologies and Optimization Techniques (ICEECCOT). IEEE, 2021.": "https://ieeexplore.ieee.org/document/9707927",
    "🏆 2020 Safwat, Nour El-Din, Fatma Newagy, and Ismail M. Hafez. 'Air-to-ground channel model for UAVs in dense urban environments.' IET Communications 14.6 (2020): 1016-1021.": "https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/iet-com.2019.0964",
    "🏆 2015 Safwat, Nour El-Din, Abdelhalim Zekry, and Mohamed Abouelatta. 'Avionics Full-duplex switched Ethernet (AFDX): Modeling and simulation.' 2015 32nd National Radio Science Conference (NRSC). IEEE, 2015.": "https://ieeexplore.ieee.org/document/7117841",
    "🏆 2014 Safwat, Nour El-Din, M. A. El-Dakroury, and Abdelhalim Zekry. 'The Evolution of Aircraft Data Networks.' International Journal of Computer Applications 94.11 (2014): 27-32. ": "https://www.ijcaonline.org/archives/volume94/number11/16389-5968"
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
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Approved with WTRL (Without Type Rate Licence) from ECCA (Egyptian Civil Aviation authority). 
- ✔️ more than 9 years experiance as Component Certifying Staff  under the EASA Part-145 approval
- ✔️ Good experiance in read out and analysis of Flight data recorders 
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
- ✔️ Very Good Acadmic back ground in Wireless communications.
- ✔️ Very Good experiance in acadimic research.
- ✔️ Good experiance in reviewing acadmic manuscripts.

"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python,MatLab
- 📊 Data Visulization: MS Excel
- 📚 Modeling: OPNET
- 📚 Flight Data Analysis : AGS,ADREAS,IGS,ROSE
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Workshop Avionics Engineer | EgyptAir**")
st.write("10/2010 - Present")
st.write(
    """
- ► Operating and maintenance of ATEC 5000 and ATEC series 6
- ► Release to service Aircraft Line Replacement Units under ECAA, EASA, and FAA Authority Regulations
- ► Read out and analysis of Flight data recorders. 
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Maintenance Engineer | NAtional Air Navigation Services Company**")
st.write("05/2010 - 10/2010")
st.write(
    """
- ► Operating and maintenance of navigation ground stations
"""
)

# --- Education ---
st.write('\n')
st.subheader("Education")

st.write("**- ► 2016- 2022 Doctor of Philosophy: Electrical Engineering**")
st.write( 
    """  
 -  Ain Shams University-Cairo, Egypt.
 -  Ph.D. thesis title is ( Unmanned Aerial Vehicles in 5G )
 -  This thesis focuses on air-to-ground, and air-to-air channel modeling, optimal 3D placement, and multi-UAVs deployment considering co-channel Interference
""")

st.write("**- ► 2010- 2014 Master of Secince: Electrical Engineering**")
st.write(
    """  
-  Ain Shams University-Cairo, Egypt.
-  Master thesis title is (Aircraft Data Network Simulation and Evaluation)
-  This thesis presents the evolution of Aircraft Data Networks. It discusses various Avionics data network protocols. Also, it represents a comprehensive simulation model for Avionics Full-duplex switched Ethernet (AFDX) network
""")
st.write("**- ► 2004- 2009 Bachelor of Science: Electrical Engineering**")
st.write("""
-  Ain Shams University-Cairo, Egypt.
-  Graduation Project:  Network Planning & Optimization for 2G & 3G Mobil Networks.
""")
# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Publications")
st.write("---")
for pub, link in Publications.items():
    st.write(f"[{pub}]({link})")
