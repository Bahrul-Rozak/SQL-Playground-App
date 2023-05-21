# Main packages
import streamlit as st
import pandas as pd
import sqlite3

# Database Management
connectionDatabase = sqlite3.connect("data/world.sqlite")
c = connectionDatabase.cursor()

# Fxn Make Execute


def sql_executor(rawCode):
    c.execute(rawCode)
    data = c.fetchall()
    return data

city = ['ID,', 'Name,', 'CountryCode,', 'District,', 'Population']
country = ['Code,', 'Name,', 'Continent,', 'Region,', 'SurfaceArea,', 'IndepYear,', 'Population,', 'LifeExpectancy,', 'GNP,', 'GNPOld,', 'LocalName,', 'GovernmentForm,', 'HeadOfState,', 'Capital,', 'Code2']
countryLanguage = ['CountryCode,', 'Language,', 'IsOfficial,', 'Percentage']



def main():
    st.title("SQL CODE PLAYGROUND")
    st.subheader("بِسْــــــــــــــــــمِ اللهِ الرَّحْمَنِ الرَّحِيْمِ")
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("HomePage")

        # Column and Layouts Set
        column1, column2 = st.columns(2)
        with column1:
            with st.form(key='query_form'):
                rawCode = st.text_area("INSERT YOUR SQL CODE IN HERE")
                submitCode = st.form_submit_button("EXECUTE YOUR QUERY")

            # Table of Information
            with st.expander("Table Information"):
                tableInformation = {'city':city,'country':country,'countryLanguage':countryLanguage}
                # Change to JSON
                st.json(tableInformation)
       # Result
        with column2:
            if submitCode:
                st.info("QUERY HAS BEEN SUBMITTED")
                st.code(rawCode)

                # Results
                queryResults = sql_executor(rawCode)
                with st.expander("RESULT"):
                    st.write(queryResults)
                with st.expander("PRETTY TABLE"):
                    queryDataFrame = pd.DataFrame(queryResults)
                    st.dataframe(queryDataFrame)

    else:
        st.subheader("AboutPage")


if __name__ == '__main__':
    main()
        