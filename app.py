"""
================================================================================
COURSE: Python Programming for Business Students
PROJECT: End-Term Project & Assignment 2
TOPIC: Life Insurance Premium Estimator & Quote Engine (Business Idea #16)
BRAND: Aegis Shield Life Insurance Co. Ltd. (IRDAI Reg. No. 142)
EDITION: Minimalist, De-Cluttered & Wide-Scrollbar Edition
================================================================================
"""

import streamlit as st
import datetime
import pandas as pd

# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION & CLEAN FINTECH CSS (DE-CLUTTERED + WIDE SCROLLBAR)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Aegis Shield Life | Clean Insurance Quote",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Clean Styling: Generous whitespace, de-cluttered cards & wider scrollbars
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* ---------------------------------------------------------
       1. ENHANCED & WIDER SCROLLBAR (MAIN PAGE & SIDEBAR)
       --------------------------------------------------------- */
    ::-webkit-scrollbar {
        width: 14px !important;
        height: 14px !important;
    }
    ::-webkit-scrollbar-track {
        background: #F1F5F9 !important;
        border-radius: 8px !important;
    }
    ::-webkit-scrollbar-thumb {
        background: #94A3B8 !important;
        border-radius: 8px !important;
        border: 3px solid #F1F5F9 !important;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #475569 !important;
    }
    * {
        scrollbar-width: auto !important;
        scrollbar-color: #94A3B8 #F1F5F9 !important;
    }

    /* ---------------------------------------------------------
       2. MINIMALIST SEGMENTED TABS (CLEAN & SPACIOUS)
       --------------------------------------------------------- */
    div[data-baseweb="tab-list"] {
        gap: 12px;
        background-color: #F8FAFC;
        padding: 6px;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        margin-bottom: 24px;
    }
    div[data-baseweb="tab"] {
        height: 42px;
        border-radius: 8px;
        padding: 6px 20px;
        font-weight: 600;
        font-size: 0.9rem;
        color: #475569;
        background-color: transparent;
        border: none !important;
        transition: all 0.2s ease;
    }
    div[data-baseweb="tab"]:hover {
        color: #0F172A;
        background-color: #EDF2F7;
    }
    div[aria-selected="true"] {
        background-color: #FFFFFF !important;
        color: #1E40AF !important;
        box-shadow: 0 2px 8px rgba(15, 23, 42, 0.08) !important;
        font-weight: 700 !important;
    }
    div[data-baseweb="tab-border"], div[data-baseweb="tab-highlight"] {
        display: none;
    }

    /* ---------------------------------------------------------
       3. DE-CLUTTERED MINIMALIST HEADER
       --------------------------------------------------------- */
    .clean-header {
        background: #0F172A;
        border-radius: 12px;
        padding: 20px 26px;
        color: white;
        margin-bottom: 24px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 14px;
    }
    .header-brand {
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 1.55rem;
        font-weight: 700;
        letter-spacing: -0.02em;
    }
    .header-subtext {
        font-size: 0.85rem;
        color: #94A3B8;
        margin-top: 3px;
    }
    .header-link-pill {
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: #F8FAFC !important;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }
    .header-link-pill:hover {
        background: rgba(255, 255, 255, 0.2);
    }

    /* ---------------------------------------------------------
       4. HERO PRICE DISPLAY (CLEAN FINTECH LOOK)
       --------------------------------------------------------- */
    .minimal-price-card {
        background: #F0FDF4;
        border: 1px solid #BBF7D0;
        border-radius: 12px;
        padding: 22px;
        margin-bottom: 20px;
    }
    .minimal-price-label {
        font-size: 0.78rem;
        text-transform: uppercase;
        font-weight: 700;
        color: #166534;
        letter-spacing: 0.05em;
        margin-bottom: 4px;
    }
    .minimal-price-value {
        font-size: 2.3rem;
        font-weight: 800;
        color: #14532D;
        line-height: 1.1;
    }

    /* ---------------------------------------------------------
       5. CLEAN CARDS & CALLOUTS
       --------------------------------------------------------- */
    .clean-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 18px;
        margin-bottom: 16px;
    }
    .tax-box {
        background: #EFF6FF;
        border-left: 4px solid #3B82F6;
        padding: 12px 16px;
        border-radius: 6px;
        font-size: 0.85rem;
        color: #1E40AF;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 2. ACTUARIAL BASE DATA
# -----------------------------------------------------------------------------
BASE_RATES_PER_LAKH = {
    "Term Life (i-Protect Pure Protection)": 110.0,
    "Endowment Plan (Guaranteed Returns)": 480.0,
    "Whole Life Shield (Lifelong 99 Yrs)": 260.0,
    "Child Future Plan (Education Milestone)": 390.0
}

PLAN_SUMMARIES = {
    "Term Life (i-Protect Pure Protection)": "Pure risk protection. Highest sum assured at the lowest rate, with 100% tax-free payout to nominee.",
    "Endowment Plan (Guaranteed Returns)": "Disciplined savings with guaranteed capital returns and maturity bonuses plus life cover.",
    "Whole Life Shield (Lifelong 99 Yrs)": "Permanent family legacy cover active up to age 99, passing accumulated corpus to legal heirs.",
    "Child Future Plan (Education Milestone)": "Secures college milestones with an automatic premium waiver if the parent passes away."
}

FREQUENCY_FACTORS = {
    "Annual (1 payment/year)": 1.0,
    "Monthly (12 payments/year)": 0.088,
    "Quarterly (4 payments/year)": 0.26,
    "Semi-Annual (2 payments/year)": 0.51
}

GST_RATE = 0.18


# -----------------------------------------------------------------------------
# 3. CORE ACTUARIAL CALCULATION FUNCTION
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

    gst_amount = subtotal_annual * GST_RATE
    total_annual_premium = subtotal_annual + gst_amount
    installment_premium = total_annual_premium * FREQUENCY_FACTORS[frequency]

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
        "tax_savings_estimate": tax_savings_estimate
    }


# -----------------------------------------------------------------------------
# 4. DE-CLUTTERED CORPORATE HEADER
# -----------------------------------------------------------------------------
st.markdown("""
<div class="clean-header">
    <div>
        <div class="header-brand">
            <span>🛡️</span> Aegis Shield Life Insurance
        </div>
        <div class="header-subtext">
            IRDAI Reg. No. 142 • 99.34% Claim Settlement Ratio • Over 2.8 Cr Families Protected
        </div>
    </div>
    <div style="display: flex; gap: 10px; align-items: center; flex-wrap: wrap;">
        <span style="font-size: 0.88rem; color: #E2E8F0;">📞 1800-266-7788</span>
        <a href="http://localhost:8501" target="_blank" class="header-link-pill">
            🪟 Open in New Tab ↗
        </a>
    </div>
</div>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 5. SIDEBAR: CLEAN INPUT CONFIGURATOR
# -----------------------------------------------------------------------------
st.sidebar.markdown("### 📋 Quote Configurator")

applicant_name = st.sidebar.text_input("Full Name", value="Rahul Sharma")

col_sb1, col_sb2 = st.sidebar.columns(2)
with col_sb1:
    age = st.number_input("Age", min_value=18, max_value=65, value=29)
with col_sb2:
    gender = st.radio("Gender", ["Male", "Female"], index=0)

policy_type = st.sidebar.selectbox("Insurance Plan", list(BASE_RATES_PER_LAKH.keys()), index=0)

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
    "Life Cover (Sum Assured)",
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
# 6. STREAMLINED, DE-CLUTTERED TABS (4 CLEAN TABS)
# -----------------------------------------------------------------------------
tab_quote, tab_family, tab_compare, tab_academic = st.tabs([
    "⚡ Instant Quote",
    "👨‍👩‍👧 Family Plans (Multi-Tab)",
    "⚖️ Plan Comparison",
    "🎓 Student Project & Logic"
])

# Compute primary quote
calc = calculate_insurance_premium(
    policy_type=policy_type,
    sum_assured=sum_assured,
    age=age,
    policy_term=policy_term,
    gender=gender,
    annual_income=1200000,
    is_smoker=is_smoker,
    has_critical_illness=rider_critical,
    has_accidental_death=rider_accidental,
    has_premium_waiver=rider_waiver,
    frequency=frequency,
    direct_online_discount=direct_discount
)

# -----------------------------------------------------------------------------
# TAB 1: INSTANT QUOTE (SPACIOUS & CLEAN)
# -----------------------------------------------------------------------------
with tab_quote:
    # Selected Plan Summary Box
    st.markdown(f"""
    <div class="clean-card" style="border-left: 4px solid #2563EB;">
        <div style="font-size: 1.15rem; font-weight: 700; color: #1E3A8A; margin-bottom: 2px;">
            {policy_type}
        </div>
        <div style="font-size: 0.88rem; color: #4B5563;">
            {PLAN_SUMMARIES[policy_type]}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Hero Quote Row
    col_price, col_m1, col_m2, col_m3 = st.columns([1.5, 1, 1, 1])
    with col_price:
        freq_title = frequency.split(" (")[0]
        st.markdown(f"""
        <div class="minimal-price-card">
            <div class="minimal-price-label">{freq_title} Premium Payable</div>
            <div class="minimal-price-value">₹{calc['installment_premium']:,.2f}</div>
            <div style="font-size: 0.8rem; color: #166534; margin-top: 4px;">
                ✓ Includes 18% GST • 0% Hidden Fees
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col_m1:
        st.metric("Daily Cost", f"₹{calc['daily_cost']:.1f} / day")
    with col_m2:
        st.metric("Annual Premium", f"₹{calc['total_annual_premium']:,.2f}")
    with col_m3:
        st.metric("Sec 80C Tax Saved", f"₹{calc['tax_savings_estimate']:,.0f}")

    # Tax Banner
    st.markdown(f"""
    <div class="tax-box">
        💼 <strong>Tax Benefit:</strong> Eligible for up to <strong>₹1,50,000 deduction</strong> under Section 80C (saving ~₹{calc['tax_savings_estimate']:,.0f}/year in income tax). All death benefits to nominees are 100% tax-free under Section 10(10D).
    </div>
    """, unsafe_allow_html=True)

    # Two Clean Columns: Invoice & Visual Breakdown
    col_table, col_chart = st.columns([3, 2])
    with col_table:
        st.markdown("#### 📑 Itemized Premium Breakdown")
        breakdown_items = [
            {"Component": f"Base Mortality Cover ({sum_assured_labels[sum_assured]})", "Amount": f"₹{calc['base_premium']:,.2f}"},
            {"Component": f"Age Factor ({calc['age_factor']}x for Age {age})", "Amount": f"₹{(calc['base_premium'] * (calc['age_factor'] - 1)):,.2f}" if calc['age_factor'] >= 1 else f"-₹{(calc['base_premium'] * (1 - calc['age_factor'])):,.2f}"},
            {"Component": "Smoker Risk Loading (+40%)", "Amount": f"₹{calc['smoker_loading']:,.2f}" if is_smoker else "₹0.00"},
            {"Component": "Female Longevity Rebate (-10%)", "Amount": f"-₹{calc['gender_discount']:,.2f}" if gender == "Female" else "₹0.00"},
            {"Component": "Net Underwritten Base Premium", "Amount": f"₹{calc['net_base_premium']:,.2f}"},
            {"Component": "Add-on Riders Total", "Amount": f"₹{calc['rider_cost']:,.2f}"},
            {"Component": "Direct Online Discount (-5%)", "Amount": f"-₹{calc['online_rebate']:,.2f}" if calc['online_rebate'] > 0 else "₹0.00"},
            {"Component": "Subtotal (Pre-Tax)", "Amount": f"₹{calc['subtotal_annual']:,.2f}"},
            {"Component": "GST (18%)", "Amount": f"₹{calc['gst_amount']:,.2f}"},
            {"Component": "⭐ Total Annual Premium", "Amount": f"₹{calc['total_annual_premium']:,.2f}"}
        ]
        st.table(breakdown_items)

    with col_chart:
        st.markdown("#### 📊 Premium Composition")
        st.bar_chart({
            "Net Base Cover": calc['net_base_premium'],
            "Riders": calc['rider_cost'],
            "GST (18%)": calc['gst_amount']
        })

        quote_code = f"AGS-{age}{policy_term}-{abs(hash(applicant_name)) % 90000 + 10000}"
        
        st.markdown(f"""
        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 12px; border-radius: 8px; font-size: 0.82rem; margin-top: 8px;">
            <strong>Quote Ref:</strong> <code>{quote_code}</code><br>
            <strong>Applicant:</strong> {applicant_name} ({gender}, Age {age})<br>
            <strong>Tenure:</strong> {policy_term} Years (Active till age {age + policy_term})
        </div>
        """, unsafe_allow_html=True)

        st.write("")
        btn_c1, btn_c2 = st.columns(2)
        with btn_c1:
            if st.button("🚀 Apply Now", type="primary", use_container_width=True):
                st.balloons()
                st.success("Application started! An underwriter will contact you.")
        with btn_c2:
            quote_text = f"""======================================================
               AEGIS SHIELD LIFE INSURANCE QUOTE
======================================================
Quote Ref    : {quote_code}
Date         : {datetime.date.today().strftime('%d-%b-%Y')}
Applicant    : {applicant_name} ({gender}, Age {age})
Plan         : {policy_type}
Sum Assured  : {sum_assured_labels[sum_assured]}
Duration     : {policy_term} Years
Payment Mode : {frequency}
------------------------------------------------------
Net Base     : ₹{calc['net_base_premium']:,.2f}
Riders Total : ₹{calc['rider_cost']:,.2f}
GST (18%)    : ₹{calc['gst_amount']:,.2f}
Total Annual : ₹{calc['total_annual_premium']:,.2f}
Installment  : ₹{calc['installment_premium']:,.2f}
======================================================
"""
            st.download_button(
                "📥 Download Quote",
                data=quote_text,
                file_name=f"Quote_{quote_code}.txt",
                mime="text/plain",
                use_container_width=True
            )

# -----------------------------------------------------------------------------
# TAB 2: MULTI-MEMBER FAMILY PLANS (CLEAN SUB-TABS)
# -----------------------------------------------------------------------------
with tab_family:
    st.markdown("### 👨‍👩‍👧 Family Coverage Builder")
    st.markdown("Switch between family member tabs to configure individual policies:")

    sub_self, sub_spouse, sub_child = st.tabs([
        "👤 Primary Proposer (Self)",
        "💍 Spouse Cover",
        "👶 Child Education Plan"
    ])

    with sub_self:
        st.markdown(f"**Proposer:** {applicant_name} (Age {age}, {gender})")
        sc1, sc2 = st.columns(2)
        with sc1:
            st.metric("Plan", policy_type)
        with sc2:
            st.metric("Annual Premium", f"₹{calc['total_annual_premium']:,.2f}")

    with sub_spouse:
        c_sp1, c_sp2, c_sp3 = st.columns(3)
        with c_sp1:
            spouse_name = st.text_input("Spouse Name", value="Pooja Sharma")
            spouse_age = st.number_input("Spouse Age", 18, 60, 27)
        with c_sp2:
            spouse_sum = st.selectbox("Spouse Cover", [2500000, 5000000, 10000000], index=1, format_func=lambda x: f"₹{x/100000:.0f} Lakhs")
            spouse_term = st.slider("Tenure", 10, 35, 25)
        with c_sp3:
            spouse_smoker = st.checkbox("Spouse Smoker", value=False)
            spouse_calc = calculate_insurance_premium(
                policy_type="Term Life (i-Protect Pure Protection)",
                sum_assured=spouse_sum,
                age=spouse_age,
                policy_term=spouse_term,
                gender="Female",
                annual_income=600000,
                is_smoker=spouse_smoker,
                has_critical_illness=True,
                has_accidental_death=False,
                has_premium_waiver=False,
                frequency="Annual (1 payment/year)",
                direct_online_discount=True
            )
            st.metric("Spouse Annual Premium", f"₹{spouse_calc['total_annual_premium']:,.2f}")

    with sub_child:
        c_ch1, c_ch2, c_ch3 = st.columns(3)
        with c_ch1:
            child_name = st.text_input("Child Name", value="Aarav Sharma")
            child_age = st.number_input("Child Current Age", 0, 17, 4)
        with c_ch2:
            child_sum = st.selectbox("Education Fund Goal", [1500000, 2500000, 5000000], index=1, format_func=lambda x: f"₹{x/100000:.0f} Lakhs")
            child_term = 18 - child_age
        with c_ch3:
            child_calc = calculate_insurance_premium(
                policy_type="Child Future Plan (Education Milestone)",
                sum_assured=child_sum,
                age=32,
                policy_term=child_term,
                gender="Male",
                annual_income=1200000,
                is_smoker=False,
                has_critical_illness=True,
                has_accidental_death=True,
                has_premium_waiver=True,
                frequency="Annual (1 payment/year)",
                direct_online_discount=True
            )
            st.metric("Child Plan Premium", f"₹{child_calc['total_annual_premium']:,.2f}")

    st.write("---")
    family_total = calc['total_annual_premium'] + spouse_calc['total_annual_premium'] + child_calc['total_annual_premium']
    f_c1, f_c2 = st.columns(2)
    with f_c1:
        st.metric("Total Family Shield Annual Cost", f"₹{family_total:,.2f}")
    with f_c2:
        st.metric("Combined Family Protection", f"₹{(sum_assured + spouse_sum + child_sum)/10000000:.2f} Crores")

# -----------------------------------------------------------------------------
# TAB 3: PLAN COMPARISON MATRIX
# -----------------------------------------------------------------------------
with tab_compare:
    st.markdown("### ⚖️ Side-by-Side Product Comparison")
    comp_df = pd.DataFrame([
        {
            "Plan": "Term Life (i-Protect)",
            "Core Goal": "Pure Family Financial Defense",
            "Maturity Proceeds": "Nil (Highest Protection / Lowest Cost)",
            "Death Payout": "100% Tax-Free Sum Assured",
            "Best For": "Salaried individuals, home loan borrowers"
        },
        {
            "Plan": "Endowment Plan",
            "Core Goal": "Protection + Compounding Wealth",
            "Maturity Proceeds": "Guaranteed Corpus + Annual Bonuses",
            "Death Payout": "Higher of Sum Assured or 105% premiums",
            "Best For": "Conservative investors, retirement corpus"
        },
        {
            "Plan": "Whole Life Shield",
            "Core Goal": "Lifelong Heritage up to Age 99",
            "Maturity Proceeds": "Active cover continues till age 99",
            "Death Payout": "Guaranteed tax-free inheritance to heirs",
            "Best For": "Generational wealth planning"
        },
        {
            "Plan": "Child Future Plan",
            "Core Goal": "College Education Guarantee",
            "Maturity Proceeds": "Scheduled college milestone payouts",
            "Death Payout": "Sum Assured + all future premiums waived",
            "Best For": "Parents of children aged 0 to 12 years"
        }
    ])
    st.dataframe(comp_df, use_container_width=True, hide_index=True)

# -----------------------------------------------------------------------------
# TAB 4: ACADEMIC PROJECT & LOGIC
# -----------------------------------------------------------------------------
with tab_academic:
    st.markdown("### 🎓 Academic Evaluation: Python Programming for Business Students")
    st.markdown("Documentation aligning directly with the assignment evaluation rubric:")

    with st.expander("📖 1. Business Problem & Solution"):
        st.markdown("""
        - **Business Idea:** Idea #16 (Insurance - Life Insurance Premium Estimator)
        - **Problem Solved:** Demystifies opaque insurance calculations, eliminating cart abandonment by providing transparent, real-time premium estimates.
        - **Target Customer:** Working professionals, parents, and loan borrowers needing reliable financial security.
        """)

    with st.expander("💻 2. Python Concepts Applied"):
        st.markdown("""
        | Concept | Implementation in this App |
        |---|---|
        | **Variables & Types** | `int` (Age, Term), `float` (Rates, GST), `str` (Names, Plans), `bool` (Smoker, Riders) |
        | **Dictionaries** | `BASE_RATES_PER_LAKH`, `FREQUENCY_FACTORS`, `PLAN_SUMMARIES` |
        | **Conditional Logic** | `if/elif/else` for mortality age brackets, smoking loading, female discounts |
        | **Arithmetic Operations** | Scaling per Lakh, adding riders, computing 18% GST, modal frequency factors |
        | **Functions** | `calculate_insurance_premium(...)` encapsulating business algorithms with type hints |
        """)

    with st.expander("📐 3. Mathematical Equations"):
        st.markdown(r"""
        $$\text{Base Premium} = \left(\frac{\text{Sum Assured}}{100,000}\right) \times \text{Base Plan Rate}$$
        $$\text{Net Base} = (\text{Base} \times \text{Age Factor} + \text{Smoker Loading} - \text{Female Discount}) \times \text{Term Factor}$$
        $$\text{Subtotal} = \text{Net Base} + \sum \text{Riders} - \text{Direct Online Discount}$$
        $$\text{Total Annual Premium} = \text{Subtotal} \times 1.18_{\text{GST}}$$
        $$\text{Installment} = \text{Total Annual Premium} \times \text{Frequency Factor}$$
        """)

# -----------------------------------------------------------------------------
# CLEAN FOOTER
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #94A3B8; font-size: 0.8rem; padding: 10px;">
    © 2026 Aegis Shield Life Insurance Company Limited • IRDAI Registration No. 142<br>
    <em>End-Term Project & Assignment 2 • Python Programming for Business Students</em>
</div>
""", unsafe_allow_html=True)
 
