        # Plain language summary sentence
        st.write("---")
        st.markdown(
            f"**Summary:** For a **{age}**-year-old customer opting for **{insurance_type}** "
            f"with a coverage of **₹{coverage_amount:,.2f}** under the **{risk_category}** profile, "
            f"the estimated annual premium is **₹{annual_premium:,.2f}**, leading to a total "
            f"cost of **₹{total_premium:,.2f}** over **{policy_years}** year(s)."
        )
# ==============================================================================
# SECTION 4: HOW THE CALCULATION WORKS (PRICING METHODOLOGY & FORMULA GUIDE)
# ==============================================================================
st.write("---")
with st.expander("ℹ️ How This Calculation Works (Pricing Methodology & Formula Guide)"):
    st.write(
        """
        ### Business Logic & Formula:
        1. **Base Premium** = `Coverage Amount` × `Base Rate`
           - Term Life: 0.5% (0.005)
           - Health Insurance: 1.0% (0.010)
           - Vehicle Insurance: 2.5% (0.025)
        2. **Risk Adjustment** = `Base Premium` × `Risk Multiplier`
           - Low Risk: 1.00x (Standard)
           - Medium Risk: 1.20x (+20%)
           - High Risk: 1.50x (+50%)
        3. **Age Surcharge**:
           - Age 18–30: ₹0
           - Age 31–50: ₹1,500 / year
           - Age 51–80: ₹3,000 / year
        4. **Optional Add-on Rider**:
           - Checked: +₹2,500 / year
           - Unchecked: ₹0
        5. **Annual Premium** = `Risk-Adjusted Premium` + `Age Surcharge` + `Add-on Rider`
        6. **Total Premium** = `Annual Premium` × `Policy Duration (Years)`
        """
    )
# Footer Disclaimer
st.caption(
    "Disclaimer: This calculator is designed for estimation and preliminary decision support. "
    "Actual insurance premiums are determined by licensed underwriters based on detailed medical, financial, and actuarial assessments."
)
