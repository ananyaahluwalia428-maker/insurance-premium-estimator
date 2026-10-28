# ==============================================================================
# PROJECT: INSURANCE PREMIUM ESTIMATOR
# Course: Python Programming for Business Students
# Technology: Python and Streamlit
# Description: A web-based decision support tool to calculate estimated insurance premiums
# ==============================================================================

# Step 1: Import the Streamlit library to build web interface components
import streamlit as st

# Step 2: Set page configuration (Browser tab title and layout)
st.set_page_config(page_title="Insurance Premium Estimator", page_icon="🛡️", layout="centered")

# Step 3: Display Website Title and Introductory Description
st.title("🛡️ Insurance Premium Estimator")
st.write(
    "Welcome! This interactive tool helps you estimate your insurance premium based "
    "on coverage amount, policy duration, age, risk profile, and optional add-ons."
)

# Step 4: Display Notice / Disclaimer banner
st.info(
    "📌 **Notice & Disclaimer**: Premium rates and calculations used in this estimator are "
    "hypothetical benchmark values for demonstration and planning purposes. They do not constitute a binding insurer quotation."
)

st.write("---")

# ==============================================================================
# SECTION 1: USER INPUTS
# ==============================================================================
st.header("📋 Step 1: Enter Customer & Policy Details")

# Input 1: Customer Age (Data Type: int)
# Restricts age between 18 and 80 years with default value of 30
age = st.number_input(
    "1. Customer Age (Years):",
    min_value=18,
    max_value=80,
    value=30,
    step=1,
    help="Enter customer age between 18 and 80 years."
)

# Input 2: Insurance Type (Data Type: str)
# Dropdown menu to choose one of three policy types
insurance_type = st.selectbox(
    "2. Select Insurance Type:",
    ("Term Life Insurance", "Health Insurance", "Vehicle Insurance"),
    help="Different insurance products have different baseline risk rates."
)

# Input 3: Coverage Amount in Rupees (Data Type: float)
# Number input allowing coverage selection from ₹50,000 to ₹1,00,00,000
coverage_amount = st.number_input(
    "3. Coverage Amount (₹):",
    min_value=50000.0,
    max_value=10000000.0,
    value=500000.0,
    step=50000.0,
    help="The total financial protection provided by the policy."
)

# Input 4: Policy Duration in Years (Data Type: int)
# Number input from 1 year to 30 years
policy_years = st.number_input(
    "4. Policy Duration (Years):",
    min_value=1,
    max_value=30,
    value=5,
    step=1,
    help="The number of years the policy remains active."
)

# Input 5: Customer Risk Category (Data Type: str)
# Dropdown menu to select lifestyle, health, or driving risk tier
risk_category = st.selectbox(
    "5. Customer Risk Category:",
    ("Low Risk", "Medium Risk", "High Risk"),
    help="Risk level reflects personal habits, medical history, or driving record."
)

# Input 6: Optional Additional Coverage / Add-on Rider (Data Type: bool)
# Checkbox that returns True if checked, False if unchecked
has_addon = st.checkbox(
    "6. Include Optional Add-on Rider (Critical Illness / Zero Depreciation) (+₹2,500/year)",
    value=False,
    help="Check this box to include enhanced protection for a fixed annual charge."
)

st.write("---")

# ==============================================================================
# SECTION 2: BUSINESS LOGIC AND CALCULATION (TRIGGERED BY BUTTON)
# ==============================================================================

# Action Button to perform calculation
calculate_button = st.button("Calculate Estimated Premium")

if calculate_button:
    # -------------------------------------------------------------------------
    # Input Validation: Ensure all inputs are logically positive and valid
    # -------------------------------------------------------------------------
    if age < 18 or age > 80:
        st.error("Error: Customer age must be between 18 and 80 years.")
    elif coverage_amount <= 0:
        st.error("Error: Coverage amount must be greater than zero.")
    elif policy_years <= 0:
        st.error("Error: Policy duration must be at least 1 year.")
    else:
        # Rule 1: Determine Base Premium Rate according to Insurance Type
        # Data Type: float
        if insurance_type == "Term Life Insurance":
            base_rate = 0.005  # 0.5% of coverage amount
        elif insurance_type == "Health Insurance":
            base_rate = 0.010  # 1.0% of coverage amount
        else:
            base_rate = 0.025  # 2.5% of coverage amount (Vehicle Insurance)

        # Rule 2: Determine Risk Multiplier according to Risk Category
        # Data Type: float
        if risk_category == "Low Risk":
            risk_multiplier = 1.00  # Normal base rate (0% extra)
        elif risk_category == "Medium Risk":
            risk_multiplier = 1.20  # 20% surcharge
        else:
            risk_multiplier = 1.50  # 50% surcharge for high risk

        # Rule 3: Determine Age-Based Surcharge (Seniority Adjustment)
        # Data Type: float
        if age <= 30:
            age_surcharge = 0.0      # Young policyholder: standard rate
        elif age <= 50:
            age_surcharge = 1500.0   # Middle-age adjustment: ₹1,500/year
        else:
            age_surcharge = 3000.0   # Senior adjustment: ₹3,000/year

        # Rule 4: Add-on Rider Cost
        # Data Type: float
        if has_addon:
            addon_cost = 2500.0      # Fixed annual fee if checkbox is checked
        else:
            addon_cost = 0.0         # No extra fee if unchecked

        # ---------------------------------------------------------------------
        # Arithmetic Calculations
        # ---------------------------------------------------------------------
        # Step A: Calculate initial base premium from coverage amount
        base_premium = coverage_amount * base_rate

        # Step B: Apply risk category multiplier
        risk_adjusted_premium = base_premium * risk_multiplier

        # Step C: Calculate total estimated annual premium
        annual_premium = risk_adjusted_premium + age_surcharge + addon_cost

        # Step D: Calculate total premium across the entire policy duration
        total_premium = annual_premium * policy_years

        # ======================================================================
        # SECTION 3: DISPLAY RESULTS
        # ======================================================================
        st.header("📊 Premium Estimation Summary")

        # Display key metrics in neat summary boxes
        st.success(f"### Estimated Annual Premium: ₹{annual_premium:,.2f}")
        st.info(f"### Estimated Total Premium ({policy_years} Years): ₹{total_premium:,.2f}")

        st.subheader("Detailed Cost Breakdown")
        st.write(f"- **Selected Insurance Type:** {insurance_type}")
        st.write(f"- **Coverage Amount:** ₹{coverage_amount:,.2f}")
        st.write(f"- **Policy Duration:** {policy_years} Year(s)")
        st.write(f"- **Customer Age:** {age} Years")
        st.write(f"- **Risk Category:** {risk_category} (Multiplier: {risk_multiplier}x)")
        st.write(f"- **Base Premium ({base_rate * 100:.1f}%):** ₹{base_premium:,.2f}")
        st.write(f"- **Risk-Adjusted Premium:** ₹{risk_adjusted_premium:,.2f}")
        st.write(f"- **Age Surcharge:** ₹{age_surcharge:,.2f}")
        st.write(f"- **Optional Add-on Rider:** ₹{addon_cost:,.2f}")

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
