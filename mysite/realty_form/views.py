from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage


# Create your views here.
def index(request):
    if(request.POST.get('submit_btn')):
        #Customer info        
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        street = request.POST.get('street', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zipcode = request.POST.get('zip', '')
        email = request.POST.get('email', '')
        phone1 = request.POST.get('phone1', '')
        phone2 = request.POST.get('phone2', '')

        #Loan Info
        bk = request.POST.get('shortsales', '')
        us_citizen = request.POST.getlist('uscitizen')
        last_investment_average = request.POST.get('last_investment_average', '')
        credit_score = request.POST.get('credit_score', '')
        purchase_price = request.POST.get('purchase_price', '')
        down_payment = request.POST.get('down_payment', '')
        loan_amount = request.POST.get('loan_amount', '')
        market_value = request.POST.get('market_value', '')
        rehab_amount = request.POST.get('rehan_amount', '')
        rehab_in_loan = request.POST.getlist('rehab_in_loan')
        arv = request.POST.get('arv', '')
        total_cost = request.POST.get('total_cost', '')
        loan_type = request.POST.get('loan_type', '')
        date_to_close = request.POST.get('date_to_close', '')
        refi_date = request.POST.get('refi', '')
        property_type = request.POST.get('property_type', '')
        investments_lifetime = request.POST.get('investments_lifetime', '')
        investments_12mo = request.POST.get('investments_12mo', '')
        investments_6mo = request.POST.get('investments_6mo', '')
        entity = request.POST.get('entity', '')
        title = request.POST.get('title', '')
        quote_sent = request.POST.get('quote_sent', '')

        #Rental Info
        monthly_rental_income = request.POST.get('monthly_rental_income', '')
        monthly_personal_income = request.POST.get('monthly_mersonal_income', '')

        #Miscellaneous
        inside_sales = request.POST.get('inside_sales', '')
        last_contacted_date = request.POST.get('last_contacted_date', '')
        loan_officer = request.POST.get('loan_officer', '')
        contact_id = request.POST.get('contact_id', '')
        preq_app_taken = request.POST.get('preq_app_taken', '')
        preq_status = request.POST.get('preq_status', '')
        notes = request.POST.get('notes', '')

        #Helpers
        fullname = first_name + " " + last_name
        address = street + ", " + city + ", " + state + ", " + zipcode
        if 'us_citizen' in us_citizen:
            us_citizen = 'yes'
        else:
            us_citizen = 'no'

        if 'rehabinloan' in rehab_in_loan:
            rehab_in_loan = 'yes'
        else:
            rehab_in_loan = 'no'        
        
        subject = first_name + " " + last_name + " " + "loan application"
        message = """
        <br><br>
        <h3>Customer Info</h3>
        <br><br>
        
        Name: {} <br>
        Address: {} <br>
        Email: {} <br>
        Phone 1: {} <br>
        Phone 2 {} <br>

         <br> <br>
        <h3>Loan Information</h3>
         <br> <br>

        Bk, shortsales, or foreclosures in the last 24 months: {} <br>
        Us Citizen: {} <br>
        Average price of last investments: ${} <br>
        Average credit score: {} <br>
        Purchase price: ${} <br>
        Down payment: ${} <br>
        Loan amount: ${} <br>
        Market Value: ${} <br>
        Rehab amount: ${} <br>
        Include rehab in loan: {} <br>
        After Repair Value (ARV): ${} <br>
        Total cost: ${} <br>
        Loan Type: {} <br>
        Date to close: {} <br>
        Refi or purchase date: {} <br>
        Property type: {} <br>
        Investments Lifetime: {} <br>
        Investments 12mo: {} <br>
        Investments 6mo: {} <br>
        Entity: {} <br>
        Title: {} <br>
        Quote Sent: {} <br>
        
        <br> <br>
        <h3>Rentals</h3>
         <br> <br>

        Monthly rental income: ${} <br>
        Monthly Personal Income: ${} <br>
        
         <br> <br>
        <h3>Miscellaneous</h3>
         <br> <br>

        Inside Sales: {} <br>
        Last contacted date: {} <br>
        Loan Officer: {} <br>
        Contact ID: {} <br>
        PreQ App Taken: {} <br>
        PreQ Status: {} <br>
        Notes: {}""".format(fullname, address, email, phone1, phone2,
                            bk, us_citizen, last_investment_average,
                            credit_score, purchase_price, down_payment,
                            loan_amount, market_value, rehab_amount,
                            rehab_in_loan, arv, total_cost, loan_type,
                            date_to_close, refi_date, property_type,
                            investments_lifetime, investments_12mo,
                            investments_6mo, entity, title, quote_sent,
                            monthly_rental_income, monthly_personal_income,
                            inside_sales, last_contacted_date, loan_officer,
                            contact_id, preq_app_taken, preq_status, notes)
        

        
        msg = EmailMessage(subject, message, 'thequadehunter@gmail.com', ['thequadehunter@gmail.com'])
        msg.content_subtype = 'html'
        msg.send()
    
    return render(request, 'realty_form/home.html')
