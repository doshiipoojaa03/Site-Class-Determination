import streamlit as st

def render_site_class_table():

    st.markdown(
        """
        <style>
        .custom-table {
            width: 70%;
            margin: auto;
            border-collapse: collapse;
            font-family: serif;
            font-size: 16px;
            text-align: center;
        }
        .custom-table th, .custom-table td {
            border: 1px solid black;
            padding: 8px;
        }
        .custom-table thead th {
            font-weight: bold;
        }
        .title {
            text-align: center;
            font-weight: bold;
            font-size: 18px;
            margin-bottom: 5px;
        }
        .subtitle {
            text-align: center;
            font-style: italic;
            margin-bottom: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="title">
            Table 4 Site Classes for Estimating Normalised PSA
        </div>
        <div class="subtitle">
            [Clause 6.2.3.1(a)]
        </div>

        <table class="custom-table">
            <thead>
                <tr>
                    <th>Sl No.</th>
                    <th>Site Class</th>
                    <th>Weighted Average Shear Wave Velocity V<sub>s</sub> (m/s)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>i)</td>
                    <td>A</td>
                    <td>1500 ≤ V<sub>s</sub></td>
                </tr>
                <tr>
                    <td>ii)</td>
                    <td>B</td>
                    <td>760 ≤ V<sub>s</sub> &lt; 1500</td>
                </tr>
                <tr>
                    <td>iii)</td>
                    <td>C</td>
                    <td>360 ≤ V<sub>s</sub> &lt; 760</td>
                </tr>
                <tr>
                    <td>iv)</td>
                    <td>D</td>
                    <td>180 ≤ V<sub>s</sub> &lt; 360</td>
                </tr>
                <tr>
                    <td>v)</td>
                    <td>E</td>
                    <td>V<sub>s</sub> ≤ 180</td>
                </tr>
            </tbody>
        </table>
        """,
        unsafe_allow_html=True
    )
