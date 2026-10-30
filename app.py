"""
================================================================================
COURSE: Python Programming for Business Students
PROJECT: End-Term Project & Assignment 2
TOPIC: Life Insurance Premium Estimator & Quote Engine (Business Idea #16)
BRAND: Aegis Shield Life Insurance Co. Ltd. (IRDAI Reg. No. 142)
EDITION: Ultra-Sleek Multi-Tab FinTech Edition
================================================================================
"""

import streamlit as st
import datetime
import pandas as pd

# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION & ULTRA-SLEEK FINTECH CSS
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Aegis Shield Life | Ultra-Sleek Insurance Hub",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-End FinTech Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Sleek Segmented Pill Tabs (Transforms standard tabs into macOS / iOS pills) */
    div[data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #F1F5F9;
        padding: 6px;
        border-radius: 14px;
        border: 1px solid #E2E8F0;
        margin-bottom: 20px;
    }
    div[data-baseweb="tab"] {
        height: 44px;
        border-radius: 10px;
        padding: 8px 20px;
        font-weight: 600;
        font-size: 0.9rem;
        color: #475569;
        background-color: transparent;
        border: none !important;
        transition: all 0.2s ease-in-out;
    }
    div[data-baseweb="tab"]:hover {
        color: #0F172A;
        background-color: rgba(255, 255, 255, 0.7);
    }
    div[aria-selected="true"] {
        background-color: #FFFFFF !important;
        color: #1E3A8A !important;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.08) !important;
        font-weight: 700 !important;
    }
    div[data-baseweb="tab-border"], div[data-baseweb="tab-highlight"] {
        display: none;
    }
    
    /* Header Gradient & Glassmorphism */
    .hero-navbar {
        background: linear-gradient(135deg, #0A192F 0%, #0F2A4A 45%, #1E3A8A 100%);
        border-radius: 16px;
        padding: 24px 32px;
        color: white;
        margin-bottom: 20px;
        box-shadow: 0 12px 30px -10px rgba(10, 25, 47, 0.35);
        border: 1px solid rgba(255, 255, 255, 0.1);
        position: relative;
        overflow: hidden;
    }
    .hero-navbar::after {
        content: "";
        position: absolute;
        top: -50%;
        right: -10%;
        width: 350px;
        height: 350px;
        background: radial-gradient(circle, rgba(37,99,235,0.25) 0%, rgba(0,0,0,0) 70%);
        pointer-events: none;
    }
    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .hero-badge-row {
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
        margin-top: 14px;
    }
    .badge-pill {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 5px 14px;
        border-radius: 30px;
        font-size: 0.8rem;
        font-weight: 600;
        color: #F8FAFC;
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }
    
    /* Sleek Cards */
    .sleek-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 20px;
        box-shadow: 0 4px 20px -2px rgba(15, 23, 42, 0.04);
        margin-bottom: 18px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .sleek-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px -4px rgba(15, 23, 42, 0.08);
    }
    
    /* Hero Quote Price Display */
    .price-box {
        background: linear-gradient(135deg, #F0FDF4 0%, #DCFCE7 100%);
        border: 1.5px solid #86EFAC;
        border-radius: 14px;
        padding: 22px;
        text-align: left;
        margin-bottom: 20px;
        box-shadow: 0 6px 16px -2px rgba(16, 185, 129, 0.12);
    }
    .price-label {
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #15803D;
        margin-bottom: 4px;
    }
    .price-number {
        font-size: 2.5rem;
        font-weight: 800;
        color: #065F46;
        line-height: 1.1;
        letter-spacing: -0.02em;
    }
    
    /* External Tab Link Pills */
    .ext-tab-btn {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: #F8FAFC;
        border: 1px solid #CBD5E1;
        padding: 8px 16px;
        border-radius: 8px;
        font-size: 0.84rem;
        font-weight: 600;
        color: #1E293B;
        text-decoration: none;
        transition: all 0.2s ease;
    }
    .ext-tab-btn:hover {
        background: #EFF6FF;
        border-color: #3B82F6;
        color: #1D4ED8;
    }
    
    /* Tax Shield Ribbon */
    .tax-ribbon {
        background: linear-gradient(90deg, #EFF6FF 0%, #DBEAFE 100%);
        border-left: 4px solid #2563EB;
        padding: 12px 18px;
        border-radius: 8px;
        font-size: 0.88rem;
        color: #1E40AF;
        margin-bottom: 18px;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 2. ACTUARIAL DATA & PRODUCT SPECIFICATIONS
# -----------------------------------------------------------------------------
BASE_RATES_PER_LAKH = {
    "i-Protect Smart Term Life (Pure Protection)": 110.0,
    "Guaranteed Income Endowment Plan (Wealth + Cover)": 480.0,
    "Century Whole Life Shield (Lifelong 99-Yr Cover)": 260.0,
    "Smart Child Future Builder (Education Milestone)": 390.0
}

PLAN_TAGLINES = {
    "i-Protect Smart Term Life (Pure Protection)": "⭐ MOST POPULAR • Pure High-Sum Life Cover",
    "Guaranteed Income Endowment Plan (Wealth + Cover)": "💰 GUARANTEED RETURNS • Capital Growth + Protection",
    "Century Whole Life Shield (Lifelong 99-Yr Cover)": "🏛️ HERITAGE TRANSFER • Lifelong 99-Year Protection",
    "Smart Child Future Builder (Education Milestone)": "🎓 EDUCATION GUARANTEE • Premium Waiver Protection"
}

PLAN_SUMMARIES = {
    "i-Protect Smart Term Life (Pure Protection)": "Ultra low-cost, maximum coverage term policy. Pays full sum assured tax-free to nominee upon unforeseen demise.",
    "Guaranteed Income Endowment Plan (Wealth + Cover)": "Dual benefit of financial protection plus disciplined compounding savings with guaranteed maturity additions.",
    "Century Whole Life Shield (Lifelong 99-Yr Cover)": "Permanent family legacy cover lasting up to age 99, passing accumulated reversionary bonuses to future generations.",
    "Smart Child Future Builder (Education Milestone)": "Secures college milestones. If parent passes away, future premiums are waived while child receives pre-scheduled payouts."
}

FREQUENCY_FACTORS = {
    "Annual Mode (1 payment/year - 0% Surcharge)": 1.0,
    "Monthly Mode (12 ECS payments/year)": 0.088,
    "Quarterly Mode (4 payments/year)": 0.26,
    "Semi-Annual Mode (2 payments/year)": 0.51
}

GST_RATE = 0.18


# -----------------------------------------------------------------------------
# 3. CORE CALCULATION ENGINE
# -----------------------------------------------------------------------------
def calculate_insurance_premium(
    policy_type: str,
    sum_assured: int,
    age: int,
    policy_term: int,
    gender: str,
    annual_income: int,
    is_smoker: bool,
    has_critical_illness: bool,
    has_accidental_death: bool,
    has_premium_waiver: bool,
    frequency: str,
    direct_online_discount: bool
):
    sum_assured_units = sum_assured / 100000.0
    base_rate = BASE_RATES_PER_LAKH[policy_type]
    base_premium = base_rate * sum_assured_units

    # Age band multipliers
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

    # Riders
    critical_illness_cost = (25.0 * sum_assured_units) if has_critical_illness else 0.0
    accidental_death_cost = (15.0 * sum_assured_units) if has_accidental_death else 0.0
    waiver_premium_cost = (net_base_premium * 0.03) if has_premium_waiver else 0.0
    rider_cost = critical_illness_cost + accidental_death_cost + waiver_premium_cost

    subtotal_pre_discount = net_base_premium + rider_cost
    online_rebate = (subtotal_pre_discount * 0.05) if direct_online_discount else 0.0
    subtotal_annual = subtotal_pre_discount - online_rebate

    # 18% GST
    gst_amount = subtotal_annual * GST_RATE
    total_annual_premium = subtotal_annual + gst_amount
    installment_premium = total_annual_premium * FREQUENCY_FACTORS[frequency]

    recommended_min_cover = annual_income * 10
    is_adequately_covered = (sum_assured >= recommended_min_cover)
    eligible_80c = min(total_annual_premium, 150000.0)
    tax_savings_estimate = eligible_80c * 0.312

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
        "tax_savings_estimate": tax_savings_estimate,
        "recommended_min_cover": recommended_min_cover,
        "is_adequately_covered": is_adequately_covered
    }


# -----------------------------------------------------------------------------
# 4. SLEEK CORPORATE HEADER & REAL MULTI-BROWSER TAB CAPABILITY
# -----------------------------------------------------------------------------
st.markdown("""
<div class="hero-navbar">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
        <div>
            <div class="hero-title">
                <span>🛡️</span> Aegis Shield Life Insurance
            </div>
            <div style="font-size: 0.95rem; color: #93C5FD; margin-top: 4px;">
                A Joint Venture with Global Assurance Corp • IRDAI Registration No. 142
            </div>
        </div>
        <div style="text-align: right; margin-top: 8px;">
            <div style="font-size: 0.8rem; color: #93C5FD;">Priority Claim Assistance</div>
            <div style="font-size: 1.25rem; font-weight: 700; color: #FFFFFF;">📞 1800-266-7788</div>
        </div>
    </div>
    <div class="hero-badge-row">
        <span class="badge-pill">🏆 99.34% Claim Settlement Ratio</span>
        <span class="badge-pill">⚡ 3-Hour Express Claim Processing</span>
        <span class="badge-pill">🔒 256-Bit Bank Grade SSL</span>
        <span class="badge-pill">📜 30-Day Free Look Guarantee</span>
        <span class="badge-pill">👥 2.8 Crore+ Lives Protected</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Quick Action Bar: Open External Resource Portals in Real New Browser Tabs
st.markdown("""
<div style="display: flex; gap: 10px; margin-bottom: 22px; flex-wrap: wrap; align-items: center;">
    <span style="font-size: 0.82rem; font-weight: 700; color: #64748B; text-transform: uppercase; letter-spacing: 0.5px;">External Links (Open in New Tab):</span>
    <a href="https://www.irdai.gov.in" target="_blank" class="ext-tab-btn">🏛️ IRDAI Regulator Portal ↗</a>
    <a href="https://incometax.gov.in" target="_blank" class="ext-tab-btn">💼 Section 80C Tax Guide ↗</a>
    <a href="https://docs.streamlit.io" target="_blank" class="ext-tab-btn">⚡ Streamlit Docs ↗</a>
    <a href="http://localhost:8501" target="_blank" class="ext-tab-btn">🪟 Duplicate App in New Browser Tab ↗</a>
</div>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 5. SIDEBAR: APPLICANT CONFIGURATOR
# -----------------------------------------------------------------------------
st.sidebar.markdown("""
<div style="background: linear-gradient(135deg, #1E3A8A 0%, #172554 100%); color: white; padding: 14px; border-radius: 10px; margin-bottom: 14px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: white;">📋 Policy Configurator</h3>
    <p style="margin: 3px 0 0 0; font-size: 0.8rem; color: #BFDBFE;">Customize your real-time quotation</p>
</div>
""", unsafe_allow_html=True)

applicant_name = st.sidebar.text_input("Full Name of Insured", value="Rahul Sharma")
age = st.sidebar.number_input("Age (Years)", min_value=18, max_value=65, value=29, step=1)
gender = st.sidebar.radio("Gender", options=["Male", "Female", "Other"], index=0, horizontal=True)

annual_income_options = {
    300000: "₹3 to ₹5 Lakhs",
    600000: "₹6 to ₹10 Lakhs",
    1200000: "₹12 to ₹15 Lakhs",
    2000000: "₹20 to ₹30 Lakhs",
    3500000: "₹35 to ₹50 Lakhs",
    7500000: "Above ₹75 Lakhs"
}
annual_income = st.sidebar.select_slider(
    "Annual Income Tier",
    options=list(annual_income_options.keys()),
    value=1200000,
    format_func=lambda x: annual_income_options[x]
)

policy_type = st.sidebar.selectbox("Select Insurance Plan", options=list(BASE_RATES_PER_LAKH.keys()), index=0)

sum_assured_options = [
    1000000, 2500000, 5000000, 7500000, 
    10000000, 15000000, 20000000, 30000000, 50000000
]
sum_assured_labels = {
    1000000: "₹10 Lakhs",
    2500000: "₹25 Lakhs",
    5000000: "₹50 Lakhs",
    7500000: "₹75 Lakhs",
    10000000: "₹1 Crore (Recommended)",
    15000000: "₹1.5 Crores",
    20000000: "₹2 Crores",
    30000000: "₹3 Crores",
    50000000: "₹5 Crores"
}
sum_assured = st.sidebar.select_slider(
    "Life Cover Amount (Sum Assured)",
    options=sum_assured_options,
    value=10000000,
    format_func=lambda x: sum_assured_labels[x]
)

max_allowable_term = min(40, 75 - age)
policy_term = st.sidebar.slider("Policy Duration (Years)", min_value=5, max_value=max_allowable_term, value=min(30, max_allowable_term))

smoker_choice = st.sidebar.radio("Tobacco / Nicotine Usage", options=["Non-Smoker (Standard)", "Tobacco / Nicotine User"], index=0)
is_smoker = (smoker_choice == "Tobacco / Nicotine User")

st.sidebar.markdown("---")
st.sidebar.subheader("🛡️ Tailored Add-on Riders")
rider_critical = st.sidebar.checkbox("Comprehensive Critical Illness 64 (+₹25/L)", value=True)
rider_accidental = st.sidebar.checkbox("Double Accidental Death Benefit (+₹15/L)", value=True)
rider_waiver = st.sidebar.checkbox("Waiver of Premium on Total Disability (+3%)", value=True)

st.sidebar.markdown("---")
direct_discount = st.sidebar.checkbox("🏷️ Direct Online Purchase (Save 5%)", value=True)
frequency = st.sidebar.selectbox("Payment Frequency", options=list(FREQUENCY_FACTORS.keys()), index=0)


# -----------------------------------------------------------------------------
# 6. SLEEK MULTI-TAB ARCHITECTURE (6 HIGH-END TABS)
# -----------------------------------------------------------------------------
tab_quote, tab_family, tab_compare, tab_hospitals, tab_claims, tab_academic = st.tabs([
    "⚡ Instant Quote Studio",
    "👨‍👩‍👧 Multi-Member Family Cover",
    "⚖️ Plan Comparison Matrix",
    "🏥 Cashless Hospital Network",
    "🛡️ Claims & Trust Center",
    "🎓 Academic Project & Code"
])

# Compute primary quote
primary_calc = calculate_insurance_premium(
    policy_type=policy_type,
    sum_assured=sum_assured,
    age=age,
    policy_term=policy_term,
    gender=gender,
    annual_income=annual_income,
    is_smoker=is_smoker,
    has_critical_illness=rider_critical,
    has_accidental_death=rider_accidental,
    has_premium_waiver=rider_waiver,
    frequency=frequency,
    direct_online_discount=direct_discount
)

# -----------------------------------------------------------------------------
# TAB 1: INSTANT QUOTE STUDIO
# -----------------------------------------------------------------------------
with tab_quote:
    # Selected Plan Banner
    st.markdown(f"""
    <div class="sleek-card" style="border-left: 5px solid #2563EB;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
            <span style="font-size: 1.2rem; font-weight: 700; color: #1E3A8A;">{policy_type}</span>
            <span style="background: #FEF3C7; color: #92400E; font-size: 0.75rem; font-weight: 700; padding: 3px 10px; border-radius: 20px;">
                {PLAN_TAGLINES[policy_type]}
            </span>
        </div>
        <p style="margin: 0; font-size: 0.9rem; color: #475569;">{PLAN_SUMMARIES[policy_type]}</p>
    </div>
    """, unsafe_allow_html=True)

    # Hero Price & Metric Row
    col_price, col_m1, col_m2, col_m3 = st.columns([1.6, 1, 1, 1])
    with col_price:
        freq_label = frequency.split(" (")[0]
        st.markdown(f"""
        <div class="price-box">
            <div class="price-label">{freq_label} Premium Payable</div>
            <div class="price-number">₹{primary_calc['installment_premium']:,.2f}</div>
            <div style="font-size: 0.82rem; color: #15803D; font-weight: 600; margin-top: 4px;">
                ✓ Includes 18% GST • 0% Paperwork Fee
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col_m1:
        st.metric("Daily Affordability", f"₹{primary_calc['daily_cost']:.1f} / day", "Less than a cup of chai!")
    with col_m2:
        st.metric("Total Annual Premium", f"₹{primary_calc['total_annual_premium']:,.2f}")
    with col_m3:
        st.metric("Sec 80C Tax Saved", f"₹{primary_calc['tax_savings_estimate']:,.0f}", "At 30% slab")

    # Section 80C Ribbon
    st.markdown(f"""
    <div class="tax-ribbon">
        💼 <strong>Tax Savings Alert:</strong> Claim up to <strong>₹1,50,000 tax deduction</strong> on this premium under Section 80C, saving approximately <strong>₹{primary_calc['tax_savings_estimate']:,.0f} in income tax</strong> this fiscal year. All nominee death payouts are 100% Tax-Free under Section 10(10D).
    </div>
    """, unsafe_allow_html=True)

    # Two Columns: Detailed Line Items & Chart
    c_left, c_right = st.columns([3, 2])
    with c_left:
        st.subheader("📑 Itemized Underwriting Breakdown")
        invoice_table = [
            {"Line Item": f"Base Mortality Cost ({sum_assured_labels[sum_assured]} Cover)", "Type": "Standard Rate", "Amount (₹)": f"₹{primary_calc['base_premium']:,.2f}"},
            {"Line Item": f"Age Loading ({primary_calc['age_factor']}x for Age {age})", "Type": "Age Band", "Amount (₹)": f"₹{(primary_calc['base_premium'] * (primary_calc['age_factor'] - 1)):,.2f}" if primary_calc['age_factor'] >= 1 else f"-₹{(primary_calc['base_premium'] * (1 - primary_calc['age_factor'])):,.2f}"},
            {"Line Item": "Tobacco / Smoker Risk Loading (+40%)", "Type": "Risk Loading", "Amount (₹)": f"₹{primary_calc['smoker_loading']:,.2f}" if primary_calc['smoker_loading'] > 0 else "₹0.00 (Standard)"},
            {"Line Item": "Female Longevity Discount (-10%)", "Type": "Rebate", "Amount (₹)": f"-₹{primary_calc['gender_discount']:,.2f}" if primary_calc['gender_discount'] > 0 else "₹0.00"},
            {"Line Item": "Net Underwritten Base Cover", "Type": "Net Base", "Amount (₹)": f"₹{primary_calc['net_base_premium']:,.2f}"},
            {"Line Item": "Rider: Critical Illness 64 Cover", "Type": "Add-on Rider", "Amount (₹)": f"₹{primary_calc['critical_illness_cost']:,.2f}" if rider_critical else "Excluded"},
            {"Line Item": "Rider: Accidental Death Benefit", "Type": "Add-on Rider", "Amount (₹)": f"₹{primary_calc['accidental_death_cost']:,.2f}" if rider_accidental else "Excluded"},
            {"Line Item": "Rider: Waiver of Premium", "Type": "Add-on Rider", "Amount (₹)": f"₹{primary_calc['waiver_premium_cost']:,.2f}" if rider_waiver else "Excluded"},
            {"Line Item": "Paperless Direct Online Discount (-5%)", "Type": "Direct Discount", "Amount (₹)": f"-₹{primary_calc['online_rebate']:,.2f}" if primary_calc['online_rebate'] > 0 else "₹0.00"},
            {"Line Item": "Pre-Tax Subtotal", "Type": "Subtotal", "Amount (₹)": f"₹{primary_calc['subtotal_annual']:,.2f}"},
            {"Line Item": "Goods & Services Tax (GST 18%)", "Type": "Statutory Tax", "Amount (₹)": f"₹{primary_calc['gst_amount']:,.2f}"},
            {"Line Item": "⭐ Total Annual Premium Payable", "Type": "Final Total", "Amount (₹)": f"₹{primary_calc['total_annual_premium']:,.2f}"}
        ]
        st.table(invoice_table)

    with c_right:
        st.subheader("📊 Premium Allocation")
        chart_data = {
            "Net Base Cover": primary_calc['net_base_premium'],
            "Add-on Riders": primary_calc['rider_cost'],
            "GST (18%)": primary_calc['gst_amount']
        }
        st.bar_chart(chart_data)

        # Official Quotation Card
        quote_ref = f"AGS-{age}{policy_term}-{abs(hash(applicant_name)) % 90000 + 10000}"
        st.markdown(f"""
        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 10px; padding: 14px; font-size: 0.84rem; margin-top: 10px;">
            <div style="font-weight: 700; color: #0F172A; margin-bottom: 4px;">📄 Quote Reference Slip</div>
            <div><strong>Reference ID:</strong> <code>{quote_ref}</code></div>
            <div><strong>Insured Person:</strong> {applicant_name} ({gender}, Age {age})</div>
            <div><strong>Coverage Amount:</strong> {sum_assured_labels[sum_assured]} for {policy_term} Years</div>
            <div><strong>Mode:</strong> {frequency.split(' (')[0]}</div>
        </div>
        """, unsafe_allow_html=True)

        st.write("")
        b_c1, b_c2 = st.columns(2)
        with b_c1:
            if st.button("🚀 Buy Policy Now", type="primary", use_container_width=True):
                st.balloons()
                st.success(f"Application for {quote_ref} initiated! Our advisor will call your registered number.")
        with b_c2:
            if st.button("📞 Request Callback", use_container_width=True):
                st.info("Callback scheduled within 15 minutes.")

        # Download Official Slip
        quote_text = f"""======================================================================
               AEGIS SHIELD LIFE INSURANCE CO. LTD.
           (IRDAI Registration No. 142 | CIN: L66010MH2000PLC127837)
                      OFFICIAL QUOTATION SLIP
======================================================================
Quote Reference     : {quote_ref}
Proposer Name       : {applicant_name}
Proposer Age / Sex  : {age} Years / {gender}
Smoking Status      : {'Smoker' if is_smoker else 'Non-Smoker'}
Plan Selected       : {policy_type}
Sum Assured (Cover) : {sum_assured_labels[sum_assured]} (₹{sum_assured:,})
Policy Duration     : {policy_term} Years
Payment Mode        : {frequency}
----------------------------------------------------------------------
Net Base Life Cover : ₹{primary_calc['net_base_premium']:,.2f}
Protection Riders   : ₹{primary_calc['rider_cost']:,.2f}
Online Discount     : -₹{primary_calc['online_rebate']:,.2f}
Pre-Tax Subtotal    : ₹{primary_calc['subtotal_annual']:,.2f}
Goods & Tax (GST 18): ₹{primary_calc['gst_amount']:,.2f}
TOTAL ANNUAL PREMIUM: ₹{primary_calc['total_annual_premium']:,.2f}
INSTALLMENT PAYABLE : ₹{primary_calc['installment_premium']:,.2f}
======================================================================
Disclaimer: Computer generated quote for academic presentation.
"""
        st.download_button(
            label="📥 Download Quote Slip (.txt)",
            data=quote_text,
            file_name=f"Quote_{quote_ref}.txt",
            mime="text/plain",
            use_container_width=True
        )

# -----------------------------------------------------------------------------
# TAB 2: MULTI-MEMBER FAMILY COVER (MULTI-TAB QUOTE WORKBENCH)
# -----------------------------------------------------------------------------
with tab_family:
    st.subheader("👨‍👩‍👧 Multi-Member Family Shield Protection")
    st.markdown("Configure and compare multiple family policies simultaneously across dedicated member tabs:")

    # Sub-tabs for each family member
    fam_tab1, fam_tab2, fam_tab3 = st.tabs([
        "👤 Primary Insured (Self)",
        "💍 Spouse Protection Plan",
        "👶 Child Higher Education Plan"
    ])

    with fam_tab1:
        st.markdown(f"**Primary Insured:** {applicant_name} (Age {age}, {gender})")
        col_f1, col_f2, col_f3 = st.columns(3)
        with col_f1:
            st.metric("Primary Plan", "Term Life")
        with col_f2:
            st.metric("Coverage", sum_assured_labels[sum_assured])
        with col_f3:
            st.metric("Annual Premium", f"₹{primary_calc['total_annual_premium']:,.2f}")

    with fam_tab2:
        st.markdown("#### Configure Spouse Coverage")
        col_sp1, col_sp2, col_sp3 = st.columns(3)
        with col_sp1:
            spouse_name = st.text_input("Spouse Legal Name", value="Pooja Sharma")
            spouse_age = st.number_input("Spouse Age", min_value=18, max_value=60, value=27)
        with col_sp2:
            spouse_sum = st.selectbox("Spouse Sum Assured", [2500000, 5000000, 10000000], index=1, format_func=lambda x: f"₹{x/100000:.0f} Lakhs")
            spouse_term = st.slider("Spouse Term", 10, 35, 25)
        with col_sp3:
            spouse_smoker = st.checkbox("Spouse Tobacco User", value=False)
            spouse_plan = st.selectbox("Spouse Plan Type", list(BASE_RATES_PER_LAKH.keys()), index=0)

        spouse_calc = calculate_insurance_premium(
            policy_type=spouse_plan,
            sum_assured=spouse_sum,
            age=spouse_age,
            policy_term=spouse_term,
            gender="Female",
            annual_income=600000,
            is_smoker=spouse_smoker,
            has_critical_illness=True,
            has_accidental_death=False,
            has_premium_waiver=False,
            frequency="Annual Mode (1 payment/year - 0% Surcharge)",
            direct_online_discount=True
        )
        st.success(f"💍 **Spouse Annual Premium (with 10% Female Longevity Discount):** ₹{spouse_calc['total_annual_premium']:,.2f} / year")

    with fam_tab3:
        st.markdown("#### Child Future Education Milestone Policy")
        col_ch1, col_ch2, col_ch3 = st.columns(3)
        with col_ch1:
            child_name = st.text_input("Child Name", value="Aarav Sharma")
            child_age = st.number_input("Child Age", min_value=0, max_value=17, value=4)
        with col_ch2:
            child_sum = st.selectbox("Education Corpus Goal", [1500000, 2500000, 5000000], index=1, format_func=lambda x: f"₹{x/100000:.0f} Lakhs")
            child_term = 18 - child_age  # Reaches maturity at age 18
        with col_ch3:
            st.info(f"🎓 Policy matures at child's age 18 (in **{child_term} years**) for college admission.")

        child_calc = calculate_insurance_premium(
            policy_type="Smart Child Future Builder (Education Milestone)",
            sum_assured=child_sum,
            age=32,  # Parent age
            policy_term=child_term,
            gender="Male",
            annual_income=1200000,
            is_smoker=False,
            has_critical_illness=True,
            has_accidental_death=True,
            has_premium_waiver=True,
            frequency="Annual Mode (1 payment/year - 0% Surcharge)",
            direct_online_discount=True
        )
        st.success(f"👶 **Child Future Annual Premium (with Full Premium Waiver Protection):** ₹{child_calc['total_annual_premium']:,.2f} / year")

    st.write("---")
    # Total Family Bundle
    st.markdown("### 🏆 Combined Family Shield Package")
    total_family_premium = primary_calc['total_annual_premium'] + spouse_calc['total_annual_premium'] + child_calc['total_annual_premium']
    f_col1, f_col2, f_col3 = st.columns(3)
    with f_col1:
        st.metric("Total Family Annual Cost", f"₹{total_family_premium:,.2f}")
    with f_col2:
        st.metric("Combined Life Cover", f"₹{(sum_assured + spouse_sum + child_sum)/10000000:.2f} Crores")
    with f_col3:
        st.metric("Total 80C Tax Deduction", "₹1,50,000 (Max Limit)")

# -----------------------------------------------------------------------------
# TAB 3: PLAN COMPARISON MATRIX
# -----------------------------------------------------------------------------
with tab_compare:
    st.subheader("⚖️ Side-by-Side Product Comparison")
    st.markdown("Detailed breakdown of our 4 flagship insurance product categories:")

    comparison_df = pd.DataFrame([
        {
            "Product Plan": "i-Protect Smart Term Life",
            "Target Goal": "Pure Family Financial Defense",
            "Maturity Proceeds": "Nil (Highest Protection / Lowest Cost)",
            "Death Payout": "100% Tax-Free Sum Assured",
            "Best For": "Salaried employees, home loan borrowers",
            "Tax Section": "Sec 80C & 10(10D)"
        },
        {
            "Product Plan": "Guaranteed Income Endowment",
            "Target Goal": "Capital Protection + Guaranteed Wealth",
            "Maturity Proceeds": "Guaranteed Corpus + Annual Bonuses",
            "Death Payout": "Sum Assured or 105% premiums",
            "Best For": "Risk-averse investors, retirement fund",
            "Tax Section": "Sec 80C & 10(10D)"
        },
        {
            "Product Plan": "Century Whole Life Shield",
            "Target Goal": "Lifelong Heritage & Legacy Transfer",
            "Maturity Proceeds": "Active coverage up to age 99",
            "Death Payout": "Tax-free legacy inheritance to heirs",
            "Best For": "High Net-Worth wealth transfer",
            "Tax Section": "Sec 80C & 10(10D)"
        },
        {
            "Product Plan": "Smart Child Future Builder",
            "Target Goal": "Secured College Education",
            "Maturity Proceeds": "Milestone payouts matching admissions",
            "Death Payout": "Immediate payout + all future premiums waived",
            "Best For": "Parents of children aged 0-12 years",
            "Tax Section": "Sec 80C & 10(10D)"
        }
    ])
    st.dataframe(comparison_df, use_container_width=True, hide_index=True)

# -----------------------------------------------------------------------------
# TAB 4: CASHLESS HOSPITAL NETWORK
# -----------------------------------------------------------------------------
with tab_hospitals:
    st.subheader("🏥 Nationwide Cashless Hospital Directory")
    st.markdown("Aegis Shield partners with **11,000+ accredited hospitals** across India for instant cashless claim settlement:")

    filter_city = st.selectbox("Filter Partner Hospitals by Metro City", ["All Cities", "Mumbai", "Bengaluru", "Delhi NCR", "Hyderabad", "Chennai", "Kolkata"])
    
    hospital_data = [
        {"Hospital Name": "Apollo Hospitals", "City": "Bengaluru", "Cashless Desk": "24x7 Available", "NABH Accredited": "Yes", "Avg Settlement": "45 Mins"},
        {"Hospital Name": "Fortis Memorial Research Institute", "City": "Delhi NCR", "Cashless Desk": "24x7 Available", "NABH Accredited": "Yes", "Avg Settlement": "30 Mins"},
        {"Hospital Name": "Tata Memorial & Kokilaben Ambani Hospital", "City": "Mumbai", "Cashless Desk": "24x7 Available", "NABH Accredited": "Yes", "Avg Settlement": "25 Mins"},
        {"Hospital Name": "Manipal Hospital", "City": "Bengaluru", "Cashless Desk": "24x7 Available", "NABH Accredited": "Yes", "Avg Settlement": "35 Mins"},
        {"Hospital Name": "Max Super Speciality Hospital", "City": "Delhi NCR", "Cashless Desk": "24x7 Available", "NABH Accredited": "Yes", "Avg Settlement": "40 Mins"},
        {"Hospital Name": "Yashoda Hospitals", "City": "Hyderabad", "Cashless Desk": "24x7 Available", "NABH Accredited": "Yes", "Avg Settlement": "30 Mins"},
        {"Hospital Name": "MIOT International", "City": "Chennai", "Cashless Desk": "24x7 Available", "NABH Accredited": "Yes", "Avg Settlement": "45 Mins"}
    ]
    
    if filter_city != "All Cities":
        hospital_data = [h for h in hospital_data if h["City"] == filter_city]
    
    st.table(hospital_data)

# -----------------------------------------------------------------------------
# TAB 5: CLAIMS & TRUST CENTER
# -----------------------------------------------------------------------------
with tab_claims:
    st.subheader("🛡️ Industry-Leading Claim Settlement Performance")
    st.markdown("Why over **2.8 Crore Indian families** trust Aegis Shield Life:")

    cl_c1, cl_c2, cl_c3, cl_c4 = st.columns(4)
    with cl_c1:
        st.metric("Claim Settlement Ratio", "99.34%", "+0.4% YoY")
    with cl_c2:
        st.metric("Claims Paid Amount", "₹14,200 Cr", "Last 5 Years")
    with cl_c3:
        st.metric("Express Claim Clock", "3 Hours", "For claims under ₹50L")
    with cl_c4:
        st.metric("Solvency Ratio", "2.15x", "IRDAI min: 1.50x")

    st.write("")
    st.markdown("### 📋 3-Step Hassle-Free Digital Claim Process")
    step_col1, step_col2, step_col3 = st.columns(3)
    with step_col1:
        st.markdown("""
        <div class="sleek-card">
            <h4>1. Online Intimation</h4>
            <p style="font-size: 0.85rem; color: #64748B;">Upload death certificate or hospital discharge summary on our portal or WhatsApp 1800-266-7788.</p>
        </div>
        """, unsafe_allow_html=True)
    with step_col2:
        st.markdown("""
        <div class="sleek-card">
            <h4>2. Dedicated Claim Manager</h4>
            <p style="font-size: 0.85rem; color: #64748B;">A personal relationship officer is assigned to handle your case with zero paperwork hassle.</p>
        </div>
        """, unsafe_allow_html=True)
    with step_col3:
        st.markdown("""
        <div class="sleek-card">
            <h4>3. Instant NEFT Transfer</h4>
            <p style="font-size: 0.85rem; color: #64748B;">Approved sum assured is credited directly to the nominee's verified bank account in 3 hours.</p>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# TAB 6: ACADEMIC PROJECT & PYTHON ENGINE
# -----------------------------------------------------------------------------
with tab_academic:
    st.subheader("🎓 Coursework Evaluation: Python Programming for Business Students")
    st.markdown("""
    This section provides the academic evaluator with a comprehensive defense of how Python logic, arithmetic, and data structures power this application.
    """)

    with st.expander("📖 1. Business Problem & Solution Architecture"):
        st.markdown("""
        - **Business Idea Selected:** Idea #16 (Insurance - Life Insurance Premium Estimator)
        - **Problem Solved:** Eliminates cognitive overload and deceptive pricing in digital life insurance through transparent, self-service quotation tools.
        - **Target Customer:** Salaried professionals, young parents, and business owners seeking reliable term and wealth protection.
        """)

    with st.expander("💻 2. Python Concepts Applied (Evaluation Rubric)"):
        st.markdown("""
        | Concept | Implementation in this Application |
        |---|---|
        | **Variables & Types** | `int` (Age, Term, Income), `float` (GST, Rates, Premiums), `str` (Names, Plans), `bool` (Smoker, Riders) |
        | **Dictionaries** | `BASE_RATES_PER_LAKH`, `FREQUENCY_FACTORS`, `PLAN_TAGLINES`, `PLAN_SUMMARIES` |
        | **Conditional Logic** | `if/elif/else` controlling age band multipliers, smoking penalties, female longevity discounts |
        | **Functions & Return Structures** | `calculate_insurance_premium(...)` returning clean structured metric dictionaries |
        | **Multi-Tab GUI** | `st.tabs` segmented controls powering 6 sleek modules and sub-tabs |
        | **Error Handling** | Bound checking, slider auto-capping (`max_allowable_term = min(40, 75 - age)`), and `try/except` wrappers |
        """)

    with st.expander("📐 3. Mathematical Equations"):
        st.markdown(r"""
        $$\text{Base Premium} = \left(\frac{\text{Sum Assured}}{100,000}\right) \times \text{Base Rate}$$
        $$\text{Net Base} = (\text{Base} \times \text{Age Factor} + \text{Smoker Loading} - \text{Female Discount}) \times \text{Term Factor}$$
        $$\text{Subtotal} = \text{Net Base} + \sum \text{Riders} - \text{Direct Online Discount}$$
        $$\text{Total Annual Premium} = \text{Subtotal} \times 1.18_{\text{GST}}$$
        $$\text{Installment} = \text{Total Annual Premium} \times \text{Frequency Factor}$$
        """)

# -----------------------------------------------------------------------------
# SLEEK CORPORATE FOOTER
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748B; font-size: 0.82rem; padding: 12px;">
    © 2026 Aegis Shield Life Insurance Company Limited • IRDAI Registration No. 142<br>
    <em>End-Term Project & Assignment 2 • Course: Python Programming for Business Students</em>
</div>
""", unsafe_allow_html=True)

