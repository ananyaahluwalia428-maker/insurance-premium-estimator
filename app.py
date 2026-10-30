"""
================================================================================
COURSE: Python Programming for Business Students
PROJECT: End-Term Project & Assignment 2
TOPIC: Life Insurance Premium Estimator (Business Idea #16)
EDITION: High-Contrast Minimalist Single-Page Edition (Fixed Header Visibility)
================================================================================
"""

import streamlit as st
import datetime

# -----------------------------------------------------------------------------
# 1. PAGE SETUP & HIGH-CONTRAST MINIMALIST CSS
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Aegis Life | Premium Estimator",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# High-contrast styling: Guarantees visibility in both Light Mode and Dark Mode
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* ---------------------------------------------------------
       1. WIDE, EASY-TO-GRAB SCROLLBAR
       --------------------------------------------------------- */
    ::-webkit-scrollbar {
        width: 14px !important;
        height: 14px !important;
    }
    ::-webkit-scrollbar-track {
        background: #F1F5F9 !important;
    }
    ::-webkit-scrollbar-thumb {
        background: #94A3B8 !important;
        border-radius: 8px !important;
        border: 3px solid #F1F5F9 !important;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #64748B !important;
    }
    * {
        scrollbar-width: auto !important;
        scrollbar-color: #94A3B8 #F1F5F9 !important;
    }

    /* ---------------------------------------------------------
       2. HIGH-CONTRAST HEADER (GUARANTEED VISIBILITY)
       --------------------------------------------------------- */
    .calm-header {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%) !important;
        border: 1px solid #334155 !important;
        border-radius: 14px !important;
        padding: 22px 28px !important;
        margin-bottom: 24px !important;
        display: flex !important;
        justify-content: space-between !important;
        align-items: center !important;
        flex-wrap: wrap !important;
        gap: 14px !important;
        box-shadow: 0 4px 14px rgba(15, 23, 42, 0.15) !important;
    }
    .calm-title {
        font-size: 1.85rem !important;
        font-weight: 800 !important;
        color: #FFFFFF !important; /* Pure high-contrast white */
        letter-spacing: -0.02em !important;
        margin: 0 !important;
        display: flex !important;
        align-items: center !important;
        gap: 10px !important;
    }
    .calm-subtitle {
        font-size: 0.9rem !important;
        color: #CBD5E1 !important; /* Crisp light silver text */
        margin-top: 5px !important;
    }
    .calm-badge {
        font-size: 0.82rem !important;
        color: #F8FAFC !important;
        background: rgba(255, 255, 255, 0.12) !important;
        border: 1px solid rgba(255, 255, 255, 0.25) !important;
        padding: 6px 14px !important;
        border-radius: 20px !important;
        font-weight: 600 !important;
    }

    /* ---------------------------------------------------------
       3. HERO PRICE CARD (SOFT & CLEAR)
       --------------------------------------------------------- */
    .hero-price-card {
        background: #F0FDF4 !important;
        border: 1.5px solid #BBF7D0 !important;
        border-radius: 12px !important;
        padding: 22px 24px !important;
        margin-bottom: 20px !important;
    }
    .hero-price-label {
        font-size: 0.8rem !important;
        text-transform: uppercase !important;
        font-weight: 700 !important;
        color: #166534 !important;
        letter-spacing: 0.05em !important;
        margin-bottom: 4px !important;
    }
    .hero-price-value {
        font-size: 2.3rem !important;
        font-weight: 800 !important;
        color: #14532D !important;
        line-height: 1.15 !important;
    }
    .hero-price-note {
        font-size: 0.82rem !important;
        color: #15803D !important;
        margin-top: 6px !important;
        font-weight: 600 !important;
    }

    /* ---------------------------------------------------------
       4. SOFT PLAN & TAX NOTICES
       --------------------------------------------------------- */
    .soft-card {
        background: #FFFFFF !important;
        border: 1px solid #CBD5E1 !important;
        border-radius: 10px !important;
        padding: 16px 18px !important;
        margin-bottom: 16px !important;
    }
    .soft-tax-note {
        background: #EFF6FF !important;
        border-left: 4px solid #3B82F6 !important;
        padding: 12px 16px !important;
        border-radius: 6px !important;
        font-size: 0.86rem !important;
        color: #1E40AF !important;
        margin-bottom: 18px !important;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 2. ACTUARIAL BASE DATA
# -----------------------------------------------------------------------------
BASE_RATES_PER_LAKH = {
    "Term Life (Pure Protection)": 110.0,
    "Endowment Plan (Savings + Protection)": 480.0,
    "Whole Life Shield (Coverage till 99 Yrs)": 260.0,
    "Child Future Plan (Education Milestone)": 390.0
}

PLAN_DESCRIPTIONS = {
    "Term Life (Pure Protection)": "Affordable, high-coverage protection. Pays full sum assured to your nominee in case of untimely demise.",
    "Endowment Plan (Savings + Protection)": "Combines life insurance with disciplined savings, providing a guaranteed maturity corpus plus life cover.",
    "Whole Life Shield (Coverage till 99 Yrs)": "Lifelong peace of mind covering you up to age 99, passing an accumulated legacy to your heirs.",
    "Child Future Plan (Education Milestone)": "Funds key educational milestones for your child, with automatic waiver of future premiums if the parent passes away."
}

FREQUENCY_FACTORS = {
    "Annual Mode (1 payment/year)": 1.0,
    "Monthly Mode (12 payments/year)": 0.088,
    "Quarterly Mode (4 payments/year)": 0.26,
    "Semi-Annual Mode (2 payments/year)": 0.51
}

GST_RATE = 0.18


# -----------------------------------------------------------------------------
# 3. CORE CALCULATION LOGIC (PYTHON ARITHMETIC & CONDITIONALS)
# -----------------------------------------------------------------------------
def calculate_insurance_premium(
    policy_type: str,
    sum_assured: int,
    age: int,
    policy_term: int,
    gender: str,
    is_smoker: bool,
    has_critical_illness: bool,
    has_accidental_death: bool,
    has_premium_waiver: bool,
    frequency: str,
    direct_online_discount: bool
):
    """Computes premium with age factors, lifestyle surcharges, riders, and GST."""
    sum_assured_units = sum_assured / 100000.0
    base_rate = BASE_RATES_PER_LAKH[policy_type]
    base_premium = base_rate * sum_assured_units

    # Age band multipliers (conditional logic)
    if age < 25:
        age_factor = 0.85
    elif 25 <= age <= 35:
        age_factor = 1.00
    elif 36 <= age <= 45:
        age_factor = 1.35
    elif 46 <= age <= 55:
        age_factor = 1.80
    else:
        age_factor = 2.40

    adjusted_premium = base_premium * age_factor
    smoker_loading = (adjusted_premium * 0.40) if is_smoker else 0.0
    gender_discount = (adjusted_premium * 0.10) if gender == "Female" else 0.0

    # Policy term factor
    if policy_term > 25:
        term_factor = 1.05
    elif policy_term < 15:
        term_factor = 0.95
    else:
        term_factor = 1.00

    net_base_premium = (adjusted_premium + smoker_loading - gender_discount) * term_factor

    # Protection riders
    critical_illness_cost = (25.0 * sum_assured_units) if has_critical_illness else 0.0
    accidental_death_cost = (15.0 * sum_assured_units) if has_accidental_death else 0.0
    waiver_premium_cost = (net_base_premium * 0.03) if has_premium_waiver else 0.0
    rider_cost = critical_illness_cost + accidental_death_cost + waiver_premium_cost

    subtotal_pre_discount = net_base_premium + rider_cost
    online_rebate = (subtotal_pre_discount * 0.05) if direct_online_discount else 0.0
    subtotal_annual = subtotal_pre_discount - online_rebate

    # 18% GST and modal frequency
    gst_amount = subtotal_annual * GST_RATE
    total_annual_premium = subtotal_annual + gst_amount
    installment_premium = total_annual_premium * FREQUENCY_FACTORS[frequency]

    eligible_80c = min(total_annual_premium, 150000.0)
    tax_savings_estimate = eligible_80c * 0.312  # approx 30% slab saving

    return {
        "base_premium": base_premium,
        "age_factor": age_factor,
        "smoker_loading": smoker_loading,
        "gender_discount": gender_discount,
        "net_base_premium": net_base_premium,
        "critical_illness_cost": critical_illness_cost,
        "accidental_death_cost": accidental_death_cost,
        "waiver_premium_cost": waiver_premium_cost,
        "rider_cost": rider_cost,
        "online_rebate": online_rebate,
        "subtotal_annual": subtotal_annual,
        "gst_amount": gst_amount,
        "total_annual_premium": total_annual_premium,
        "installment_premium": installment_premium,
        "daily_cost": total_annual_premium / 365.0,
        "tax_savings_estimate": tax_savings_estimate
    }


# -----------------------------------------------------------------------------
# 4. HIGH-CONTRAST HEADER (100% VISIBLE BRAND NAME)
# -----------------------------------------------------------------------------
st.markdown("""
<div class="calm-header">
    <div>
        <div class="calm-title">
            <span>🛡️</span> Aegis Life Insurance
        </div>
        <div class="calm-subtitle">
            Simple, transparent premium calculation with instant itemized quotes
        </div>
    </div>
    <div style="display: flex; gap: 8px; align-items: center;">
        <span class="calm-badge">IRDAI Reg. No. 142</span>
        <span class="calm-badge">99.3% Claim Ratio</span>
    </div>
</div>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 5. SIDEBAR CONFIGURATOR (CLEAN, UNCLUTTERED INPUTS)
# -----------------------------------------------------------------------------
st.sidebar.markdown("### 📋 Your Details")

applicant_name = st.sidebar.text_input("Full Name", value="Rahul Sharma")

col_sb1, col_sb2 = st.sidebar.columns(2)
with col_sb1:
    age = st.sidebar.number_input("Age", min_value=18, max_value=65, value=29)
with col_sb2:
    gender = st.sidebar.radio("Gender", ["Male", "Female"], index=0, horizontal=True)

policy_type = st.sidebar.selectbox("Choose Plan", list(BASE_RATES_PER_LAKH.keys()), index=0)

sum_assured_options = [1000000, 2500000, 5000000, 7500000, 10000000, 15000000, 20000000]
sum_assured_labels = {
    1000000: "₹10 Lakhs",
    2500000: "₹25 Lakhs",
    5000000: "₹50 Lakhs",
    7500000: "₹75 Lakhs",
    10000000: "₹1 Crore",
    15000000: "₹1.5 Crores",
    20000000: "₹2 Crores"
}
sum_assured = st.sidebar.select_slider(
    "Coverage Amount (Sum Assured)",
    options=sum_assured_options,
    value=10000000,
    format_func=lambda x: sum_assured_labels[x]
)

max_term = min(40, 75 - age)
policy_term = st.sidebar.slider("Policy Duration (Years)", min_value=5, max_value=max_term, value=min(25, max_term))

is_smoker = (st.sidebar.radio("Tobacco Usage", ["Non-Smoker", "Smoker (+40%)"], index=0) == "Smoker (+40%)")

st.sidebar.markdown("---")
st.sidebar.markdown("**Add-on Riders**")
rider_critical = st.sidebar.checkbox("Critical Illness Cover (+₹25/L)", value=True)
rider_accidental = st.sidebar.checkbox("Accidental Death Cover (+₹15/L)", value=True)
rider_waiver = st.sidebar.checkbox("Premium Waiver on Disability (+3%)", value=False)

st.sidebar.markdown("---")
direct_discount = st.sidebar.checkbox("Direct Online Discount (Save 5%)", value=True)
frequency = st.sidebar.selectbox("Payment Frequency", list(FREQUENCY_FACTORS.keys()), index=0)


# -----------------------------------------------------------------------------
# 6. MAIN SINGLE-PAGE OUTPUT (ZERO TABS - DIRECT, CALM FLOW)
# -----------------------------------------------------------------------------
calc = calculate_insurance_premium(
    policy_type=policy_type,
    sum_assured=sum_assured,
    age=age,
    policy_term=policy_term,
    gender=gender,
    is_smoker=is_smoker,
    has_critical_illness=rider_critical,
    has_accidental_death=rider_accidental,
    has_premium_waiver=rider_waiver,
    frequency=frequency,
    direct_online_discount=direct_discount
)

# Plan Title & Description Card
st.markdown(f"""
<div class="soft-card">
    <div style="font-size: 1.15rem; font-weight: 700; color: #0F172A; margin-bottom: 4px;">
        {policy_type}
    </div>
    <div style="font-size: 0.9rem; color: #475569;">
        {PLAN_DESCRIPTIONS[policy_type]}
    </div>
</div>
""", unsafe_allow_html=True)

# Hero Price Card & Summary Metrics
c_price, c_m1, c_m2, c_m3 = st.columns([1.6, 1, 1, 1])

with c_price:
    freq_label = frequency.split(" (")[0]
    st.markdown(f"""
    <div class="hero-price-card">
        <div class="hero-price-label">{freq_label} Premium</div>
        <div class="hero-price-value">₹{calc['installment_premium']:,.2f}</div>
        <div class="hero-price-note">✓ Includes 18% GST • No hidden charges</div>
    </div>
    """, unsafe_allow_html=True)

with c_m1:
    st.metric("Daily Equivalent", f"₹{calc['daily_cost']:.1f} / day")
with c_m2:
    st.metric("Total Annual Cost", f"₹{calc['total_annual_premium']:,.2f}")
with c_m3:
    st.metric("Sec 80C Tax Saved", f"₹{calc['tax_savings_estimate']:,.0f}")

# Gentle Tax Note
st.markdown(f"""
<div class="soft-tax-note">
    💼 <strong>Tax Advantage:</strong> Premiums qualify for tax deductions up to ₹1,50,000 under Section 80C. Nominee death benefit payouts are 100% tax-free under Section 10(10D).
</div>
""", unsafe_allow_html=True)

# Itemized Breakdown & Chart Columns
col_left, col_right = st.columns([3, 2])

with col_left:
    st.markdown("#### Itemized Cost Breakdown")
    breakdown_data = [
        {"Component": f"Base Mortality Cover ({sum_assured_labels[sum_assured]})", "Amount": f"₹{calc['base_premium']:,.2f}"},
        {"Component": f"Age Multiplier ({calc['age_factor']}x for Age {age})", "Amount": f"₹{(calc['base_premium'] * (calc['age_factor'] - 1)):,.2f}" if calc['age_factor'] >= 1 else f"-₹{(calc['base_premium'] * (1 - calc['age_factor'])):,.2f}"},
        {"Component": "Smoker Surcharge (+40%)", "Amount": f"₹{calc['smoker_loading']:,.2f}" if is_smoker else "₹0.00"},
        {"Component": "Female Longevity Rebate (-10%)", "Amount": f"-₹{calc['gender_discount']:,.2f}" if gender == "Female" else "₹0.00"},
        {"Component": "Net Underwritten Base Premium", "Amount": f"₹{calc['net_base_premium']:,.2f}"},
        {"Component": "Add-on Riders Total", "Amount": f"₹{calc['rider_cost']:,.2f}"},
        {"Component": "Online Direct Discount (-5%)", "Amount": f"-₹{calc['online_rebate']:,.2f}" if calc['online_rebate'] > 0 else "₹0.00"},
        {"Component": "Pre-Tax Subtotal", "Amount": f"₹{calc['subtotal_annual']:,.2f}"},
        {"Component": "GST (18%)", "Amount": f"₹{calc['gst_amount']:,.2f}"},
        {"Component": "⭐ Total Annual Premium", "Amount": f"₹{calc['total_annual_premium']:,.2f}"}
    ]
    st.table(breakdown_data)

with col_right:
    st.markdown("#### Premium Composition")
    st.bar_chart({
        "Base Cover": calc['net_base_premium'],
        "Riders": calc['rider_cost'],
        "GST (18%)": calc['gst_amount']
    })

    quote_id = f"AGS-{age}{policy_term}-{abs(hash(applicant_name)) % 90000 + 10000}"
    st.markdown(f"""
    <div style="background: #F8FAFC; border: 1px solid #CBD5E1; padding: 12px 14px; border-radius: 8px; font-size: 0.85rem; margin-top: 10px; color: #1E293B;">
        <strong>Quote Ref:</strong> <code>{quote_id}</code><br>
        <strong>Applicant:</strong> {applicant_name} ({gender}, Age {age})<br>
        <strong>Term:</strong> {policy_term} Years (Active till age {age + policy_term})
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    b1, b2 = st.columns(2)
    with b1:
        if st.button("Apply for Policy", type="primary", use_container_width=True):
            st.success(f"Application for quote {quote_id} received. Our representative will contact you.")
    with b2:
        quote_text = f"""======================================================
               AEGIS LIFE INSURANCE QUOTE
======================================================
Quote ID     : {quote_id}
Date         : {datetime.date.today().strftime('%d-%b-%Y')}
Applicant    : {applicant_name} ({gender}, Age {age})
Plan         : {policy_type}
Sum Assured  : {sum_assured_labels[sum_assured]}
Duration     : {policy_term} Years
Mode         : {frequency}
------------------------------------------------------
Net Base     : ₹{calc['net_base_premium']:,.2f}
Riders Total : ₹{calc['rider_cost']:,.2f}
GST (18%)    : ₹{calc['gst_amount']:,.2f}
Total Annual : ₹{calc['total_annual_premium']:,.2f}
Installment  : ₹{calc['installment_premium']:,.2f}
======================================================
"""
        st.download_button(
            "Download Quote",
            data=quote_text,
            file_name=f"Quote_{quote_id}.txt",
            mime="text/plain",
            use_container_width=True
        )

# -----------------------------------------------------------------------------
# 7. COLLAPSIBLE ACCORDIONS (KEEPS VIEW CLEAN FOR USER, ACCESSIBLE FOR PROFESSOR)
# -----------------------------------------------------------------------------
st.write("---")

with st.expander("⚖️ Plan Comparison & Guidelines"):
    st.markdown("""
    | Plan | Best Suited For | Maturity Benefit | Nominee Benefit |
    |---|---|---|---|
    | **Term Life** | Salaried employees & home loan borrowers | Nil (Lowest cost, maximum cover) | 100% Tax-Free Sum Assured |
    | **Endowment Plan** | Conservative investors | Guaranteed Corpus + Bonuses | Full Sum Assured |
    | **Whole Life Shield** | Generational estate & legacy planning | Cover active up to age 99 | Legacy inheritance |
    | **Child Future Plan** | Parents of young children | Milestone college fund payouts | Sum Assured + Future premiums waived |
    """)

with st.expander("🎓 Academic Project Details & Python Logic (For Course Evaluation)"):
    st.markdown("""
    **Course:** Python Programming for Business Students | **Idea #16:** Insurance Premium Estimator  
    - **Variables & Types:** `int` (Age, Term), `float` (GST, Rates), `str` (Names, Plan), `bool` (Smoker, Riders)
    - **Dictionaries:** `BASE_RATES_PER_LAKH`, `PLAN_DESCRIPTIONS`, `FREQUENCY_FACTORS`
    - **Conditional Logic:** `if/elif/else` controlling age band mortality, smoking penalties, female longevity rebates
    - **Formulas:**
      $$\\text{Base} = \\left(\\frac{\\text{Sum Assured}}{100,000}\\right) \\times \\text{Rate}$$
      $$\\text{Net Base} = (\\text{Base} \\times \\text{Age Factor} + \\text{Smoker Loading} - \\text{Female Rebate}) \\times \\text{Term Factor}$$
      $$\\text{Total Premium} = (\\text{Net Base} + \\text{Riders} - \\text{Discount}) \\times 1.18_{\\text{GST}}$$
    """)

# -----------------------------------------------------------------------------
# FOOTER
# -----------------------------------------------------------------------------
st.markdown("""
<div style="text-align: center; color: #64748B; font-size: 0.78rem; padding: 20px 0;">
    © 2026 Aegis Life Insurance Co. Ltd. • IRDAI Reg. 142<br>
    <em>End-Term Project & Assignment 2 • Python Programming for Business Students</em>
</div>
""", unsafe_allow_html=True)
