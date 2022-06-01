import streamlit as st
st.set_page_config(layout="wide")

import sys
import pkg_resources
import platform
from datetime import datetime 


installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])


def info_page():
    st.write('Server Information')
    st.table([
        ['Datetime', datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        ['Operating System', " ".join([platform.system(), platform.release(), platform.version()])]
    ])

    st.write('Environment Information')
    st.table([
        ['Python version',sys.version], 
        ['Streamlit version', st.__version__], 
    ])

    st.write('Installed Packages')
    st.table(installed_packages_list)