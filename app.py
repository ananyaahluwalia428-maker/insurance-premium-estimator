"""
================================================================================
COURSE: Python Programming for Business Students
PROJECT: End-Term Project & Assignment 2
TOPIC: Life Insurance Premium Estimator & Quote Engine (Business Idea #16)
BRAND: Aegis Shield Life Insurance Co. Ltd. (IRDAI Reg. No. 142)
AUTHOR: Student Project Submission
================================================================================
"""

import streamlit as st
import datetime

# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION & CORPORATE BRAND STYLING (COMMERCIAL UI/UX)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Aegis Shield Life | India's Trusted Life Insurer",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Corporate CSS for authentic insurance portal look & feel
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Top Corporate Header */
    .corporate-header {
        background: linear-gradient(135deg, #0A192F 0%, #172A45 50%, #1E3A8A 100%);
        padding: 24px 30px;
        border-radius: 12px;
        color: white;
        margin-bottom: 20px;
        box-shadow: 0 10px 25px -5px rgba(10, 25, 47, 0.3);
    }
    .corp-title {
        font-size: 2.1rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .corp-tagline {
        font-size: 0.95rem;
        color: #93C5FD;
        margin-top: 6px;
        margin-bottom: 0;
    }
    .header-badges {
        display: flex;
        gap: 15px;
        margin-top: 14px;
        flex-wrap: wrap;
    }
    .corp-pill {
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.78rem;
        font-weight: 600;
        color: #F8FAFC;
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }
    
    /* Trust & Guarantee Strip */
    .trust-strip {
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 12px 20px;
        margin-bottom: 24px;
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        gap: 12px;
        text-align: center;
    }
    .trust-item {
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 0.85rem;
        font-weight: 600;
        color: #334155;
    }
    .trust-icon {
        color: #2563EB;
        font-size: 1.1rem;
    }

    /* Modern Quote Metric Cards */
    .quote-hero-box {
        background: linear-gradient(135deg, #F0FDF4 0%, #DCFCE7 100%);
        border: 1.5px solid #86EFAC;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgba(16, 185, 129, 0.1);
    }
    .hero-premium-title {
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 700;
        color: #15803D;
        margin-bottom: 4px;
    }
    .hero-premium-amount {
        font-size: 2.3rem;
        font-weight: 800;
        color: #065F46;
        line-height: 1.1;
    }
    
    /* Tax Saving Highlight Callout */
    .tax-badge-box {
        background: #EFF6FF;
        border-left: 4px solid #2563EB;
        padding: 12px 16px;
        border-radius: 6px;
        margin-bottom: 16px;
        font-size: 0.88rem;
        color: #1E40AF;
    }
    
    /* Plan Selection Card */
    .plan-card {
        background: #FFFFFF;
        border: 1.5px solid #CBD5E1;
        border-radius: 10px;
        padding: 16px;
        margin-bottom: 14px;
        transition: all 0.2s ease-in-out;
    }
    .badge-popular {
        background: #FEF3C7;
        color: #92400E;
        font-size: 0.72rem;
        font-weight: 700;
        padding: 2px 8px;
        border-radius: 12px;
        text-transform: uppercase;
    }

    /* Live Support Bar */
    .support-bar {
        background: #1E293B;
        color: #94A3B8;
        padding: 10px 16px;
        border-radius: 8px;
        font-size: 0.82rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 18px;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 2. BUSINESS ACTUARIAL DATA & PRODUCT SPECIFICATIONS
# -----------------------------------------------------------------------------
# Dictionary: Base annual rate per ₹1,00,000 (1 Lakh) of Sum Assured
# Derived from IRDAI standardized term & endowment morbidity mortality tables
BASE_RATES_PER_LAKH = {
    "i-Protect Smart Term Life (Pure Protection)": 110.0,
    "Guaranteed Income Endowment Plan (Wealth + Cover)": 480.0,
    "Century Whole Life Shield (Lifelong 99-Yr Cover)": 260.0,
    "Smart Child Future Builder (Education Milestone)": 390.0
}

PLAN_TAGLINES = {
    "i-Protect Smart Term Life (Pure Protection)": "⭐ Most Popular • Maximum Financial Security at Minimum Cost",
    "Guaranteed Income Endowment Plan (Wealth + Cover)": "💰 Guaranteed Maturity Corpus + Comprehensive Life Cover",
    "Century Whole Life Shield (Lifelong 99-Yr Cover)": "🏛️ Generational Legacy Transfer up to Age 99",
    "Smart Child Future Builder (Education Milestone)": "🎓 Guaranteed Education Funding with Premium Waiver Protection"
}

PLAN_SUMMARIES = {
    "i-Protect Smart Term Life (Pure Protection)": "Ideal for breadwinners. Provides high sum assured at ultra-low rates. Payout provided to nominee upon unforeseen demise during policy duration.",
    "Guaranteed Income Endowment Plan (Wealth + Cover)": "Combines capital security with disciplined savings. Payout of maturity corpus with guaranteed additions upon term completion.",
    "Century Whole Life Shield (Lifelong 99-Yr Cover)": "Provides lifelong family legacy protection till age 99. Accumulated reversionary bonuses payable to legal heirs.",
    "Smart Child Future Builder (Education Milestone)": "Secures key academic milestones. If the parent passes away, future premiums are completely waived while the child receives milestone educational payouts."
}

# Modal frequency factors (Installment multipliers)
FREQUENCY_FACTORS = {
    "Annual Mode (1 payment/year - 0% Surcharge)": 1.0,
    "Monthly Mode (12 ECS payments/year)": 0.088,
    "Quarterly Mode (4 payments/year)": 0.26,
    "Semi-Annual Mode (2 payments/year)": 0.51
}

GST_RATE = 0.18  # 18% Goods & Services Tax (IRDAI Life Insurance Directive)


# -----------------------------------------------------------------------------
# 3. CORE ACTUARIAL BUSINESS LOGIC ENGINE (PYTHON FUNCTIONS & ARITHMETIC)
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
    """
    Computes life insurance premium quotation modeled after authentic insurer underwriting:
    - Base Plan mortality charges per ₹1 Lakh sum assured
    - Multi-tier age band risk loading
    - 40% tobacco/nicotine surcharge
    - 10% female longevity discount
    - Add-on protection riders (Critical illness, Accidental death, Premium waiver)
    - 5% Direct-to-Consumer digital discount
    - Statutory 18% GST and modal installment breakdown
    """
    # Step 1: Base calculation using plan dictionary
    sum_assured_units = sum_assured / 100000.0
    base_rate = BASE_RATES_PER_LAKH[policy_type]
    base_premium = base_rate * sum_assured_units

    # Step 2: Actuarial Age Multiplier (Conditional logic)
    if age < 25:
        age_factor = 0.85     # Preferred Young Adult Tier
    elif 25 <= age <= 35:
        age_factor = 1.00     # Prime Healthy Adult Baseline
    elif 36 <= age <= 45:
        age_factor = 1.35     # Mature Risk Band
    elif 46 <= age <= 55:
        age_factor = 1.80     # Elevated Morbidity Risk
    else:
        age_factor = 2.40     # Senior Coverage Band (56-65)

    adjusted_premium = base_premium * age_factor

    # Step 3: Lifestyle Tobacco / Smoking Surcharge
    if is_smoker:
        smoker_loading = adjusted_premium * 0.40  # +40% actuarial loading
    else:
        smoker_loading = 0.0

    # Step 4: Actuarial Longevity Gender Discount
    # Statistical tables reflect higher female life expectancy
    if gender == "Female":
        gender_discount = adjusted_premium * 0.10  # 10% healthy female rebate
    else:
        gender_discount = 0.0

    # Step 5: Policy Tenure Adjustment Factor
    if policy_term > 25:
        term_factor = 1.05
    elif policy_term < 15:
        term_factor = 0.95
    else:
        term_factor = 1.00

    net_base_premium = (adjusted_premium + smoker_loading - gender_discount) * term_factor

    # Step 6: Add-on Protection Rider Charges
    rider_cost = 0.0
    critical_illness_cost = 0.0
    accidental_death_cost = 0.0
    waiver_premium_cost = 0.0

    if has_critical_illness:
        # ₹25 per Lakh cover (Covers 64 critical conditions like cancer, stroke, bypass)
        critical_illness_cost = 25.0 * sum_assured_units
        rider_cost += critical_illness_cost

    if has_accidental_death:
        # ₹15 per Lakh cover (Double payout for accidental demise)
        accidental_death_cost = 15.0 * sum_assured_units
        rider_cost += accidental_death_cost

    if has_premium_waiver:
        # 3% of net base premium to waive all future premiums upon disability
        waiver_premium_cost = net_base_premium * 0.03
        rider_cost += waiver_premium_cost

    # Step 7: Subtotal and Digital Direct Discount
    subtotal_pre_discount = net_base_premium + rider_cost
    
    online_rebate = 0.0
    if direct_online_discount:
        # 5% paperless direct purchase discount
        online_rebate = subtotal_pre_discount * 0.05

    subtotal_annual = subtotal_pre_discount - online_rebate

    # Step 8: Statutory GST Calculation
    gst_amount = subtotal_annual * GST_RATE
    total_annual_premium = subtotal_annual + gst_amount

    # Step 9: Modal Frequency Installment Calculation
    modal_factor = FREQUENCY_FACTORS[frequency]
    installment_premium = total_annual_premium * modal_factor

    # Step 10: Income Suitability Check (Human Life Value - HLV Rule of Thumb)
    # Recommended cover is 10x - 15x annual income
    recommended_min_cover = annual_income * 10
    recommended_max_cover = annual_income * 15
    is_adequately_covered = (sum_assured >= recommended_min_cover)

    # Step 11: Estimated Section 80C Tax Savings (assuming 30% tax bracket + cess)
    eligible_80c_investment = min(total_annual_premium, 150000.0)
    tax_savings_estimate = eligible_80c_investment * 0.312  # 30% slab + 4% cess

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
        "recommended_max_cover": recommended_max_cover,
        "is_adequately_covered": is_adequately_covered
    }


# -----------------------------------------------------------------------------
# 4. BRAND HEADER & TRUST BANNER
# -----------------------------------------------------------------------------
st.markdown("""
<div class="corporate-header">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
        <div>
            <div class="corp-title">
                <span>🛡️</span> Aegis Shield Life Insurance
            </div>
            <p class="corp-tagline">A Joint Venture with Global Assurance Corp • IRDAI Registration No. 142</p>
        </div>
        <div style="text-align: right; margin-top: 8px;">
            <span style="font-size: 0.8rem; color: #93C5FD; display: block;">24x7 Customer Helpline</span>
            <span style="font-size: 1.15rem; font-weight: 700; color: #FFFFFF;">📞 1800-266-7788</span>
        </div>
    </div>
    <div class="header-badges">
        <span class="corp-pill">🏆 99.34% Claim Settlement Ratio (FY 2025-26)</span>
        <span class="corp-pill">⚡ 3-Hour Express Claim Processing</span>
        <span class="corp-pill">🔒 256-Bit Bank Grade SSL Encryption</span>
        <span class="corp-pill">📜 30-Day Free-Look Money-Back Guarantee</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Trust Statistics Banner
st.markdown("""
<div class="trust-strip">
    <div class="trust-item"><span class="trust-icon">👥</span> <strong>2.8 Crore+</strong> Lives Protected</div>
    <div class="trust-item"><span class="trust-icon">💰</span> <strong>₹14,200 Cr</strong> Claims Settled</div>
    <div class="trust-item"><span class="trust-icon">⭐</span> <strong>4.8 / 5 Rating</strong> (85,000+ Reviews)</div>
    <div class="trust-item"><span class="trust-icon">🏥</span> <strong>11,000+</strong> Cashless Partner Hospitals</div>
</div>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 5. SIDEBAR: APPLICANT PROFILER & POLICY CONFIGURATOR
# -----------------------------------------------------------------------------
st.sidebar.markdown("""
<div style="background: #1E3A8A; color: white; padding: 12px; border-radius: 8px; margin-bottom: 14px;">
    <h3 style="margin: 0; font-size: 1.1rem; color: white;">📋 Get Your Instant Quote</h3>
    <p style="margin: 3px 0 0 0; font-size: 0.78rem; color: #BFDBFE;">Customize your plan parameters in real-time</p>
</div>
""", unsafe_allow_html=True)

# Input 1: Proposer Full Name
applicant_name = st.sidebar.text_input(
    "Full Name of Insured",
    value="Rahul Sharma",
    help="Enter official legal name as registered in PAN/Aadhaar."
)

# Input 2: Age with Slider and Validation
age = st.sidebar.number_input(
    "Age (Years)",
    min_value=18,
    max_value=65,
    value=29,
    step=1,
    help="Eligible age band is 18 to 65 years. Life expectancy rates adjust accordingly."
)

# Input 3: Gender Radio
gender = st.sidebar.radio(
    "Gender",
    options=["Male", "Female", "Other"],
    index=0,
    horizontal=True,
    help="Female applicants receive an automatic 10% healthy longevity discount on base rates."
)

# Input 4: Annual Income for Human Life Value underwriting
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
    format_func=lambda x: annual_income_options[x],
    help="Used to calculate Human Life Value (HLV) to ensure adequate family coverage."
)

# Input 5: Plan Selector
policy_type = st.sidebar.selectbox(
    "Select Insurance Plan",
    options=list(BASE_RATES_PER_LAKH.keys()),
    index=0,
    help="Select the insurance product architecture matching your life stage."
)

# Input 6: Sum Assured / Coverage Amount
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
    format_func=lambda x: sum_assured_labels[x],
    help="Tax-free lump sum payout to nominee upon demise under Section 10(10D)."
)

# Input 7: Policy Term Slider
max_allowable_term = min(40, 75 - age)  # Cover up to age 75 maximum
policy_term = st.sidebar.slider(
    "Policy Duration (Coverage Period)",
    min_value=5,
    max_value=max_allowable_term,
    value=min(30, max_allowable_term),
    help=f"Based on your entry age ({age}), maximum permitted coverage tenure is {max_allowable_term} years."
)

# Input 8: Smoking / Nicotine Consumption
smoker_choice = st.sidebar.radio(
    "Tobacco or Nicotine Consumption",
    options=["Non-Smoker (Clean Lifestyle)", "Tobacco / Nicotine User"],
    index=0,
    help="Non-smokers qualify for our lowest preferred rates. Smokers incur a 40% morbidity loading."
)
is_smoker = (smoker_choice == "Tobacco / Nicotine User")

# Input 9: Comprehensive Protection Riders
st.sidebar.markdown("---")
st.sidebar.subheader("🛡️ Tailored Add-on Riders")
rider_critical = st.sidebar.checkbox(
    "Comprehensive Critical Illness (+₹25/Lakh)",
    value=True,
    help="Immediate lump-sum cash payout upon diagnosis of 64 critical conditions."
)
rider_accidental = st.sidebar.checkbox(
    "Double Accidental Death Benefit (+₹15/Lakh)",
    value=True,
    help="Pays 2x the base sum assured to nominee in event of fatal accident."
)
rider_waiver = st.sidebar.checkbox(
    "Waiver of Premium on Total Disability (+3%)",
    value=True,
    help="All future premiums waived if you suffer permanent disability while cover continues."
)

# Input 10: Digital Purchase Discount & Payment Mode
st.sidebar.markdown("---")
direct_discount = st.sidebar.checkbox(
    "🏷️ Direct Online Purchase (Save 5%)",
    value=True,
    help="Zero agent commission: enjoy 5% lifetime direct discount on policy premiums."
)

frequency = st.sidebar.selectbox(
    "Premium Payment Frequency",
    options=list(FREQUENCY_FACTORS.keys()),
    index=0
)


# -----------------------------------------------------------------------------
# 6. MAIN APPLICATION TABS (COMMERCIAL USER EXPERIENCE)
# -----------------------------------------------------------------------------
tab_quote, tab_plans, tab_reviews, tab_academic = st.tabs([
    "⚡ Instant Quote & Dashboard",
    "⚖️ Plan Comparison & Features",
    "⭐ Customer Reviews & Trust",
    "🎓 Academic Project & Python Logic"
])

# -----------------------------------------------------------------------------
# TAB 1: INSTANT QUOTE & COMMERCIAL DASHBOARD
# -----------------------------------------------------------------------------
with tab_quote:
    # Validation Check
    has_error = False
    if not applicant_name.strip():
        st.error("⚠️ Please specify the Proposer Full Name in the sidebar configurator.")
        has_error = True
    
    if (age + policy_term) > 75:
        st.warning(f"⚠️ Policy tenure cannot exceed age 75. Current maturity age: {age + policy_term} years.")
        has_error = True

    if not has_error:
        try:
            # Execute Business Calculation
            calc = calculate_insurance_premium(
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

            # Selected Plan Hero Header
            st.markdown(f"""
            <div class="plan-card" style="border-left: 5px solid #2563EB;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <span style="font-size: 1.15rem; font-weight: 700; color: #1E3A8A;">{policy_type}</span>
                    <span class="badge-popular">{PLAN_TAGLINES[policy_type]}</span>
                </div>
                <p style="margin: 0; font-size: 0.9rem; color: #4B5563;">{PLAN_SUMMARIES[policy_type]}</p>
            </div>
            """, unsafe_allow_html=True)

            # Human Life Value Suitability Alert
            if not calc["is_adequately_covered"]:
                st.info(f"💡 **Underwriting Advisory:** Based on your annual income of {annual_income_options[annual_income]}, insurance experts recommend a minimum cover of **₹{calc['recommended_min_cover'] / 10000000:.1f} Crores** (10x income). You currently have selected **{sum_assured_labels[sum_assured]}**.")
            else:
                st.success(f"✅ **Optimal Coverage:** Your selected {sum_assured_labels[sum_assured]} cover perfectly aligns with your financial human life value (10x-15x income benchmark).")

            # Main Price & Metric Hero Row
            col_main_price, col_m1, col_m2, col_m3 = st.columns([1.6, 1, 1, 1])

            with col_main_price:
                freq_label = frequency.split(" (")[0]
                st.markdown(f"""
                <div class="quote-hero-box">
                    <div class="hero-premium-title">Your {freq_label} Premium</div>
                    <div class="hero-premium-amount">₹{calc['installment_premium']:,.2f}</div>
                    <div style="font-size: 0.8rem; color: #15803D; margin-top: 4px; font-weight: 600;">
                        ✓ Includes 18% GST • No Hidden Fees
                    </div>
                </div>
                """, unsafe_allow_html=True)

            with col_m1:
                st.metric("Daily Affordability", f"₹{calc['daily_cost']:.1f} / day", "Less than coffee!")
            with col_m2:
                st.metric("Total Annual Premium", f"₹{calc['total_annual_premium']:,.2f}")
            with col_m3:
                st.metric("Sec 80C Tax Saved", f"₹{calc['tax_savings_estimate']:,.0f}", "Max 30% slab")

            st.write("")

            # Section 80C Callout Box
            st.markdown(f"""
            <div class="tax-badge-box">
                💼 <strong>Income Tax Benefit:</strong> Under Section 80C, your annual premium of <strong>₹{calc['total_annual_premium']:,.2f}</strong> is fully tax-deductible up to ₹1,50,000, saving you approximately <strong>₹{calc['tax_savings_estimate']:,.0f} in income taxes</strong> each year. Plus, all death payouts to nominees are 100% tax-free under Section 10(10D).
            </div>
            """, unsafe_allow_html=True)

            # Two Column Layout: Detailed Itemized Breakdown + Commercial Actions
            col_left, col_right = st.columns([3, 2])

            with col_left:
                st.subheader("📑 Itemized Premium Quotation")
                st.caption(f"Underwriting Proposer: {applicant_name} | Age {age} | {gender} | {policy_term} Yrs Tenure")

                # Professional invoice line items
                invoice_items = [
                    {"Item Description": f"Base Life Mortality Charge ({sum_assured_labels[sum_assured]} Cover)", "Type": "Base Rate", "Amount (₹)": f"₹{calc['base_premium']:,.2f}"},
                    {"Item Description": f"Actuarial Age Loading ({calc['age_factor']}x for Age {age})", "Type": "Age Band", "Amount (₹)": f"₹{(calc['base_premium'] * (calc['age_factor'] - 1)):,.2f}" if calc['age_factor'] >= 1 else f"-₹{(calc['base_premium'] * (1 - calc['age_factor'])):,.2f}"},
                    {"Item Description": "Tobacco / Smoker Risk Loading (+40%)", "Type": "Risk Loading", "Amount (₹)": f"₹{calc['smoker_loading']:,.2f}" if calc['smoker_loading'] > 0 else "₹0.00 (Standard)"},
                    {"Item Description": "Female Longevity Discount (-10%)", "Type": "Longevity Rebate", "Amount (₹)": f"-₹{calc['gender_discount']:,.2f}" if calc['gender_discount'] > 0 else "N/A"},
                    {"Item Description": "Net Underwritten Base Premium", "Type": "Net Base", "Amount (₹)": f"₹{calc['net_base_premium']:,.2f}"},
                    {"Item Description": "Rider: 64 Critical Illness Cover", "Type": "Add-on Rider", "Amount (₹)": f"₹{calc['critical_illness_cost']:,.2f}" if rider_critical else "Excluded"},
                    {"Item Description": "Rider: Double Accidental Death Benefit", "Type": "Add-on Rider", "Amount (₹)": f"₹{calc['accidental_death_cost']:,.2f}" if rider_accidental else "Excluded"},
                    {"Item Description": "Rider: Waiver of Premium on Disability", "Type": "Add-on Rider", "Amount (₹)": f"₹{calc['waiver_premium_cost']:,.2f}" if rider_waiver else "Excluded"},
                    {"Item Description": "Paperless Direct Online Discount (-5%)", "Type": "Direct Discount", "Amount (₹)": f"-₹{calc['online_rebate']:,.2f}" if calc['online_rebate'] > 0 else "₹0.00"},
                    {"Item Description": "Taxable Subtotal (Pre-Tax)", "Type": "Subtotal", "Amount (₹)": f"₹{calc['subtotal_annual']:,.2f}"},
                    {"Item Description": "Government GST (18%)", "Type": "Statutory Tax", "Amount (₹)": f"₹{calc['gst_amount']:,.2f}"},
                    {"Item Description": "⭐ Total Annual Premium Payable", "Type": "Final Total", "Amount (₹)": f"₹{calc['total_annual_premium']:,.2f}"}
                ]
                st.table(invoice_items)

            with col_right:
                st.subheader("📊 Premium Allocation")
                # Native chart
                chart_breakdown = {
                    "Net Base Cover": calc['net_base_premium'],
                    "Protection Riders": calc['rider_cost'],
                    "GST (18%)": calc['gst_amount']
                }
                st.bar_chart(chart_breakdown)

                # Official Policy Quote Reference Card
                quote_date = datetime.date.today().strftime("%d-%B-%Y")
                quote_ref = f"AGS-{age}{policy_term}-{abs(hash(applicant_name)) % 90000 + 10000}"
                
                st.markdown(f"""
                <div style="background: #F1F5F9; border: 1px solid #CBD5E1; border-radius: 8px; padding: 14px; font-size: 0.85rem; margin-top: 10px;">
                    <div style="font-weight: 700; color: #1E293B; margin-bottom: 6px;">📄 Official Policy Quote Card</div>
                    <div><strong>Quote Ref:</strong> <code>{quote_ref}</code></div>
                    <div><strong>Generated on:</strong> {quote_date}</div>
                    <div><strong>Proposer:</strong> {applicant_name} ({gender}, Age {age})</div>
                    <div><strong>Nominee Benefit:</strong> {sum_assured_labels[sum_assured]}</div>
                    <div><strong>Duration:</strong> {policy_term} Years (Active till age {age + policy_term})</div>
                    <div><strong>Payment Mode:</strong> {frequency.split(' (')[0]}</div>
                </div>
                """, unsafe_allow_html=True)

                st.write("")

                # Commercial CTA Buttons
                col_btn1, col_btn2 = st.columns(2)
                with col_btn1:
                    if st.button("🚀 Buy Policy Now", type="primary", use_container_width=True):
                        st.balloons()
                        st.success(f"Thank you, {applicant_name}! Your application for {quote_ref} has been initiated. Our underwriter will call you at your registered mobile number for medical verification.")
                with col_btn2:
                    if st.button("📞 Request Callback", use_container_width=True):
                        st.info("A licensed insurance advisor will contact you within 15 minutes.")

                # Download Official Quotation Slip
                quote_slip_content = f"""======================================================================
               AEGIS SHIELD LIFE INSURANCE CO. LTD.
           (IRDAI Registration No. 142 | CIN: L66010MH2000PLC127837)
                      OFFICIAL QUOTATION SLIP
======================================================================
Quote Reference     : {quote_ref}
Quotation Date      : {quote_date}
Proposer Name       : {applicant_name}
Proposer Age / Sex  : {age} Years / {gender}
Smoking Status      : {'Smoker / Nicotine User' if is_smoker else 'Non-Smoker (Standard Preferred)'}
Annual Income Band  : {annual_income_options[annual_income]}
Plan Selected       : {policy_type}
Sum Assured (Cover) : {sum_assured_labels[sum_assured]} (₹{sum_assured:,})
Policy Duration     : {policy_term} Years (Coverage up to Age {age + policy_term})
Payment Mode        : {frequency}
----------------------------------------------------------------------
FINANCIAL PREMIUM BREAKDOWN:
Base Plan Mortality : ₹{calc['base_premium']:,.2f}
Age Factor ({calc['age_factor']}x)   : Included
Tobacco Surcharge   : ₹{calc['smoker_loading']:,.2f}
Female Longevity    : -₹{calc['gender_discount']:,.2f}
Net Base Life Cover : ₹{calc['net_base_premium']:,.2f}
Critical Illness 64 : ₹{calc['critical_illness_cost']:,.2f}
Accidental Benefit  : ₹{calc['accidental_death_cost']:,.2f}
Waiver of Premium   : ₹{calc['waiver_premium_cost']:,.2f}
Direct Online (-5%) : -₹{calc['online_rebate']:,.2f}
----------------------------------------------------------------------
Pre-Tax Subtotal    : ₹{calc['subtotal_annual']:,.2f}
Goods & Tax (GST 18): ₹{calc['gst_amount']:,.2f}
TOTAL ANNUAL PREMIUM: ₹{calc['total_annual_premium']:,.2f}
INSTALLMENT PAYABLE : ₹{calc['installment_premium']:,.2f}
----------------------------------------------------------------------
TAX ADVANTAGE:
• Sec 80C Eligible  : Up to ₹1,50,000 tax deduction
• Estimated Saving  : ₹{calc['tax_savings_estimate']:,.0f} per year
• Sec 10(10D)       : All death payouts 100% Tax-Free
======================================================================
Customer Support: 1800-266-7788 | support@aegisshieldlife.com
Registered Office: Aegis Towers, Bandra-Kurla Complex, Mumbai 400051
Disclaimer: Quotation generated for academic and demonstration purposes.
"""
                st.download_button(
                    label="📥 Download Official Quote Slip (.txt)",
                    data=quote_slip_content,
                    file_name=f"Aegis_Shield_Quote_{applicant_name.replace(' ', '_')}_{quote_ref}.txt",
                    mime="text/plain",
                    use_container_width=True
                )

        except Exception as e:
            st.error(f"Underwriting Engine Alert: {str(e)}")
            st.info("Please verify the entered demographic values in the sidebar.")

# -----------------------------------------------------------------------------
# TAB 2: PLAN COMPARISON & FEATURES
# -----------------------------------------------------------------------------
with tab_plans:
    st.subheader("⚖️ Compare Aegis Shield Insurance Products")
    st.markdown("Choose the right plan architecture depending on your family's financial horizon and life goals:")

    comparison_data = [
        {
            "Product Name": "i-Protect Smart Term Life",
            "Core Objective": "Pure Financial Defense",
            "Maturity Returns": "Nil (Highest Payout / Lowest Premium)",
            "Death Payout": "100% Tax-Free Sum Assured",
            "Ideal Candidate": "Salaried individuals, first-time home buyers, young parents",
            "Tax Benefits": "Sec 80C & Sec 10(10D)"
        },
        {
            "Product Name": "Guaranteed Income Endowment",
            "Core Objective": "Capital Preservation + Wealth",
            "Maturity Returns": "Guaranteed Maturity Corpus + Reversionary Bonuses",
            "Death Payout": "Higher of Sum Assured or 105% premiums paid",
            "Ideal Candidate": "Conservative investors planning retirement or college funds",
            "Tax Benefits": "Sec 80C & Sec 10(10D)"
        },
        {
            "Product Name": "Century Whole Life Shield",
            "Core Objective": "Lifelong Family Legacy",
            "Maturity Returns": "Continues active till age 99 with cash value surrender",
            "Death Payout": "Guaranteed inheritance transfer to grandchildren/heirs",
            "Ideal Candidate": "HNI legacy planners, business succession architects",
            "Tax Benefits": "Sec 80C & Sec 10(10D)"
        },
        {
            "Product Name": "Smart Child Future Builder",
            "Core Objective": "Child Higher Education",
            "Maturity Returns": "Milestone payouts matching university admissions",
            "Death Payout": "Immediate payout + all future premiums waived by insurer",
            "Ideal Candidate": "Parents with children aged 0 to 12 years",
            "Tax Benefits": "Sec 80C & Sec 10(10D)"
        }
    ]
    st.table(comparison_data)

    st.write("")
    st.subheader("🛡️ Core Pillars of Life Insurance Security")
    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown("#### 🔒 Immediate Debt Protection")
        st.write("Wipes out liabilities like home mortgages, vehicle loans, and credit debts so your family is never burdened.")
    with p2:
        st.markdown("#### 📈 Guaranteed Future Wealth")
        st.write("Disciplined annual compounding guarantees funds for university fees and family milestones regardless of market downturns.")
    with p3:
        st.markdown("#### ⚖️ Sovereign Tax Shield")
        st.write("Deduct up to ₹1.5 Lakhs every year under Section 80C. Claims and maturity proceeds are exempt under Section 10(10D).")

# -----------------------------------------------------------------------------
# TAB 3: CUSTOMER REVIEWS & TRUST
# -----------------------------------------------------------------------------
with tab_reviews:
    st.subheader("⭐ What Our Policyholders Say")
    st.markdown("Over **2.8 Crore families** trust Aegis Shield for life protection.")

    r1, r2, r3 = st.columns(3)
    with r1:
        st.markdown("""
        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 16px; border-radius: 8px;">
            <div style="color: #F59E0B; font-size: 1rem; margin-bottom: 6px;">★★★★★</div>
            <p style="font-size: 0.88rem; color: #334155; font-style: italic;">
                "Got my 1 Crore term cover in under 15 minutes! The transparent breakdown showed me exactly how my smoking status affected the premium. No hidden costs."
            </p>
            <div style="font-weight: 700; font-size: 0.85rem; color: #0F172A;">Vikramaditya Rao</div>
            <div style="font-size: 0.75rem; color: #64748B;">Senior Tech Lead, Bengaluru</div>
        </div>
        """, unsafe_allow_html=True)
    with r2:
        st.markdown("""
        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 16px; border-radius: 8px;">
            <div style="color: #F59E0B; font-size: 1rem; margin-bottom: 6px;">★★★★★</div>
            <p style="font-size: 0.88rem; color: #334155; font-style: italic;">
                "The 3-hour claim settlement guarantee gave our family peace of mind. Truly professional and the instant quotation slip was clear."
            </p>
            <div style="font-weight: 700; font-size: 0.85rem; color: #0F172A;">Priya Sundaram</div>
            <div style="font-size: 0.75rem; color: #64748B;">Chartered Accountant, Mumbai</div>
        </div>
        """, unsafe_allow_html=True)
    with r3:
        st.markdown("""
        <div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 16px; border-radius: 8px;">
            <div style="color: #F59E0B; font-size: 1rem; margin-bottom: 6px;">★★★★★</div>
            <p style="font-size: 0.88rem; color: #334155; font-style: italic;">
                "I compared 4 other companies and Aegis Shield gave the most detailed actuarial view. The female longevity discount was an awesome benefit."
            </p>
            <div style="font-weight: 700; font-size: 0.85rem; color: #0F172A;">Ananya Banerjee</div>
            <div style="font-size: 0.75rem; color: #64748B;">Marketing Director, New Delhi</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.subheader("🛡️ IRDAI Regulatory Disclosures & Compliance")
    st.info("""
    **Statutory Warning:** Insurance is the subject matter of solicitation. Please read sales brochure and policy wording carefully before concluding a sale.  
    **IRDAI Registration No.:** 142 • **CIN:** L66010MH2000PLC127837 • **Grievance Redressal Officer:** complaints@aegisshieldlife.com • Toll Free: 1800-266-7788.
    """)

# -----------------------------------------------------------------------------
# TAB 4: ACADEMIC PROJECT & PYTHON LOGIC (EVALUATION GUIDE)
# -----------------------------------------------------------------------------
with tab_academic:
    st.subheader("🎓 Coursework Information: Python Programming for Business Students")
    st.markdown("""
    This section is designed for the academic evaluator to demonstrate how Python fundamentals solve this business challenge.
    """)

    with st.expander("📖 1. Business Problem & Solution Summary"):
        st.markdown("""
        - **Business Idea Selected:** Idea #16 (Insurance - Premium Estimator)
        - **Problem Solved:** Overcomes opaque pricing, hidden surcharges, and customer cart abandonment in digital insurance by providing an instantaneous, interactive, self-service quotation engine.
        - **Target Customer:** Salaried professionals, young parents, and business owners needing reliable life coverage.
        """)

    with st.expander("💻 2. Python Concepts Applied (Rubric Alignment)"):
        st.markdown("""
        | Python Concept | Where & How Used in this Project |
        |---|---|
        | **Variables & Data Types** | `int` (Age, Term, Income), `float` (GST, Premium), `str` (Names, Plans), `bool` (Smoker, Riders) |
        | **Dictionaries** | `BASE_RATES_PER_LAKH`, `FREQUENCY_FACTORS`, `PLAN_TAGLINES`, `PLAN_SUMMARIES` |
        | **Conditional Logic (`if/elif/else`)** | Actuarial age brackets, tobacco surcharges, female discount, and boundary validation |
        | **Arithmetic Operations** | Multipliers, rider summing, subtotal discounts, 18% GST calculation, modal division |
        | **Functions & Docstrings** | `calculate_insurance_premium(...)` encapsulating business algorithms with type hints |
        | **Input Widgets (10 widgets)** | `text_input`, `number_input`, `radio`, `selectbox`, `select_slider`, `slider`, `checkbox` |
        | **Error Handling** | Bound checking (`min_value`, `max_value`), tenure capping, and `try-except` wrappers |
        """)

    with st.expander("📐 3. Mathematical Formulae"):
        st.markdown(r"""
        $$\text{Base Premium} = \left(\frac{\text{Sum Assured}}{100,000}\right) \times \text{Base Plan Rate}$$
        $$\text{Adjusted Base} = \text{Base Premium} \times \text{Age Multiplier} + \text{Smoker Loading} (40\%) - \text{Female Discount} (10\%)$$
        $$\text{Subtotal} = \text{Adjusted Base} + \sum \text{Riders} - \text{Direct Online Discount} (5\%)$$
        $$\text{Total Annual Premium} = \text{Subtotal} + (\text{Subtotal} \times 0.18_{\text{GST}})$$
        $$\text{Installment Premium} = \text{Total Annual Premium} \times \text{Frequency Factor}$$
        """)

# -----------------------------------------------------------------------------
# CORPORATE FOOTER
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748B; font-size: 0.82rem; padding: 10px;">
    © 2026 Aegis Shield Life Insurance Company Limited. All Rights Reserved. | IRDAI Regn. No. 142<br>
    <em>Academic Submission: End-Term Project & Assignment 2 • Python Programming for Business Students</em>
</div>
""", unsafe_allow_html=True)
