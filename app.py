import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyDX8os0xVmRfWDXfKR-rnaoks3_GfwtwFg"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')


def main():
    st.set_page_config(page_title="SQL Query Generator", page_icon="🤖")
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>SQL Query Generator 🤖</h1>
            <h3>Generate SQL queries with ease ✨</h3>
            <h4>With Explanation as well 📚</h4>
            <p>This app is a simple query generator that allows you to generate SQL queries with ease</p>
        </div>
        """,
        unsafe_allow_html=True
    )
     
    text_input = st.text_area("Enter your SQL query here in plain English")

    
    submit_button = st.button("Generate SQL Query")

    if submit_button:

        with st.spinner("Generating SQL Query..."):
            template = """
                Create a SQL Query snippet using the below text:
                    

                    {text_input}
                    
                    
                    I just want a SQL Query 



            """
            formatted_template = template.format(text_input=text_input)

           
            response = model.generate_content(formatted_template)
            sql_query = response.text

            sql_query = sql_query.strip().lstrip("```sql").rstrip("```")


            expected_output = """
                What would be the expected output of the SQL Query snippet:
                        '''
                    

                    {sql_query}
                    '''
                    
                    
                    Provide sample tabular Response with no explanation :

            """
            expected_output_formatted = expected_output.format(sql_query=sql_query)

            eoutput = model.generate_content(expected_output_formatted)
            eoutput = eoutput.text
       


            explanation = """
                Explain the SQL Query snippet:
                        '''
                    

                    {sql_query}
                    '''
                    
                    
                    Please provide with simplest of explanation :

            """
        explanation_formatted = explanation.format(sql_query=sql_query)
        explanation = model.generate_content(explanation_formatted)
        explanation = explanation.text

        with st.container() :
            st.success("SQL Query Generated Successfully! Here is your Query Below : ")
            st.code(sql_query, language="sql")

            st.success("Expected Output of the SQL Query : ")
            st.markdown(eoutput)

            st.success("Explanation of the SQL Query : ")
            st.markdown(explanation)


main()











