import streamlit as st

# Define responses in categorized dictionaries
procurement_and_contracts = {
    "addendum": "An addendum to a purchase order is any change in quantity, pricing, additions, or deletions to an existing purchase order, initiated by end users through a request for purchase order.",
    "amendment": "An Amendment is a legally enforceable modification to an existing agreement that is prepared or reviewed by Harris County Attorney's Office.",
    "authorized amount": "The authorized amount is the cumulative value of all work authorizations issued to a contractor, vendor, or service provider pursuant to a Purchase Order.",
    "change order": "A change order is a change in plans, specifications, price, or quantity to an existing contract, not referring to amendments prepared by Harris County Attorney's Office.",
    "contract": "A contract/agreement is a formal, written agreement executed by the County and another party, containing terms and conditions for goods and/or services to be furnished to the County."
}

capital_and_budget = {
    "capital asset": "A capital asset is County property with a unit value of $500 or more, recorded as fixed assets on the General Ledger, depreciated over its useful life, and must be recorded on Harris County Inventory Listing.",
    "capital fund": "Capital funds are provided for financing capital projects, primarily including construction bonds, commercial paper, and construction fund from revenue pool.",
    "capital project": "A capital project is an investment whose value is realized over many years, typically more than $5,000, that acquires, adds value to, or prolongs the life of a County asset.",
    "cip": "CIP stands for Capital Improvement Program, covering capital projects the County is planning, designing, and implementing over upcoming fiscal years.",
    "cost estimate": "A cost estimate is a monetary value estimated to cover the cost of all tasks and activities required to achieve the project's objective.",
    "cwip": "CWIP stands for Construction Work-In-Progress, representing the economic construction activity status for substantially incomplete buildings and other structures.",
    "encumbrance": "An encumbrance is the amount set aside in the County's Financial System to cover expenditures on a specific Purchase Order.",
    "fund budget": "Fund budget is the amount of funds available for an approved project at a given time, which may be less than the project budget.",
    "project budget": "A project budget is a monetary value estimated to cover the cost of all tasks and activities required to achieve the project's objective, based on the project cost estimate and inclusive of contingency allowance.",
    "pre-encumbrance": "A pre-encumbrance is a mid-process hold in PeopleSoft that precedes encumbrance, occurring while a requisition is in process of being approved to become a PO."
}

operations_and_maintenance = {
    "Why must a vehicle's parking brake be set while riding the Lynchburg Ferry?": "Setting your parking brake is a federal requirement from the United States Coast Guard. When traveling across the ship channel, the ferryboats can incur strong winds or currents. Without the parking brake set, vehicles can shift in transport, which is unsafe for passengers and crew.",
    "How will the Lynchburg Ferry operations and maintenance be funded?": "HCTRA operates the Lynchburg Ferry as part of its Enterprise Fund, separate from Harris County’s General Fund. Funds are sourced from Chapter 284 of the Texas Transportation Code, specifically allocated for transportation purposes including maintenance, repair, and operation of related facilities.",
    "How will the Washburn Tunnel operations and maintenance be funded?": "Similar to the Lynchburg Ferry, HCTRA manages the Washburn Tunnel under its Enterprise Fund without relying on Harris County’s General Fund. Chapter 284 of the Texas Transportation Code provides Mobility Program Funds to cover non-toll transportation needs within Harris County, ensuring ongoing maintenance and operational costs are met.",
    "Is passing allowed while driving through the Washburn Tunnel?": "No, Texas law prohibits passing in areas marked with solid double yellow lines, which are present throughout the Washburn Tunnel. Even if the opposite lane appears clear, the tunnel’s structure may limit visibility, making passing unsafe for drivers.",
    "What will change now that HCTRA is managing the Washburn Tunnel?": "Drivers will experience no significant changes as the Washburn Tunnel remains toll-free and operates 24/7. HCTRA ensures continued maintenance, weather updates, and roadside assistance through its Incident Response Team, enhancing safety and convenience for users.",
    "Why is HCTRA managing the Washburn Tunnel?": "To ensure the safety, enjoyment, and toll-free operation of this historic transportation asset for long-term public use, management of the Washburn Tunnel was transferred to HCTRA by the Harris County Commissioners Court. HCTRA’s engineering expertise and operational capabilities support ongoing modernization and maintenance efforts.",
    "Why is HCTRA managing the Lynchburg Ferry?": "To preserve the safety and future usability of this unique transportation asset, management of the Lynchburg Ferry was transferred to HCTRA by the Harris County Commissioners Court. HCTRA’s dedicated engineering and operational resources ensure ongoing maintenance and modernization while keeping the ferry toll-free for public use.",
    "What display settings allow optimal site viewing?": "The Harris County Toll Road Authority suggests setting your Display Properties no smaller than 1024x768."
}

quickbase = {
    "quickbase security": "To keep Quickbase data secure, implement role-based access control, use strong passwords, enable multi-factor authentication, regularly update permissions, and follow best practices for data security.",
    "create record": "To create a new record in Quickbase, click the '+ New Record' button in the relevant table.",
    "edit record": "To edit an existing record in Quickbase, open the record and click 'Edit' or double-click the field you want to change.",
    "delete record": "Yes, you can delete records in Quickbase if you have permission. Look for a delete option or trash can icon.",
    "search data": "To search for specific data in Quickbase, use the search bar at the top of each table or report.",
    "basic advanced search": "Basic search looks for exact matches, while advanced allows more complex queries.",
    "log in Quickbase": "To log into Quickbase, go to our company's Quickbase URL and use your employee ID as username and your network password.",
    "export excel": "To export data to Excel from Quickbase, view any report, look for the 'Export' or 'Download' button, usually in the top-right corner, and select 'Excel' as the format.",
    "quickbase url": "Our QuickBase URL is: https://harriscounty.quickbase.com",
    "what is quickbase": "Quickbase is a low-code platform for creating custom business applications. Our organization uses it to manage projects, track inventory, and automate workflows.",
    "create application": "To create a new application in Quickbase, click on the 'Create a new app' button on the home page or app bar, choose a template or start from scratch, name your app, and follow the setup wizard.",
    "export quickbase": "To export data from Quickbase, open the table, go to 'Import/Export,' select 'Export,' choose your format (CSV, Excel, etc.), select the fields to export, and click 'Export.'",
    "delete record quickbase": "To delete a record in Quickbase, locate the record, click the 'Delete' option (usually in the record menu or toolbar), confirm the deletion, and the record will be removed.",
    "search quickbase": "To search for specific records in Quickbase, use the search bar at the top of the table or report, enter your search terms (you can use operators for advanced searches), and press Enter.",
    "app vs table": "In Quickbase, an app is a collection of tables, dashboards, and reports that work together for a specific purpose. A table is a single dataset within an app, with records and fields.",
    "user permissions": "User permissions in Quickbase define what actions users can perform within an app. They can be managed by the app administrator in the 'Users' section under settings.",
    "quickbase integrations": "Quickbase can integrate with various systems using APIs, webhooks, and built-in connectors. Common integrations include CRM systems, email platforms, and project management tools.",
    "dashboard": "A dashboard in Quickbase is a customizable interface displaying data from multiple tables or reports, allowing for real-time insights and easy access to important metrics.",
    "custom formula": "To create a custom formula in Quickbase, go to the table settings, choose the field you want to calculate, select 'Formula' as the field type, and enter your formula using Quickbase's formula syntax."
}

hctra_faq = {
    "How does EZ TAG Express work?": "An EZ TAG Express account is only available with a credit card payment option and does not require a transponder. You will receive an email with instructions on how to activate your account and manage it online.",
    "How is my minimum account balance determined?": "Per the EZ TAG Agreement, the minimum EZ TAG account balance is determined based on the number of vehicles and frequency of toll usage. The minimum balance ensures that there are sufficient funds to cover tolls when you use the toll roads.",
    "How much does an EZ TAG cost?": "When you open an EZ TAG account with the required initial prepaid balance, there is no additional cost for the EZ TAG. It provides convenience and savings compared to paying tolls with cash.",
    "What if my car breaks down on the tollway?": "Please call the Incident Response Team for free roadside assistance if your car breaks down on the tollway. They will help move your vehicle to a safe location and provide minor repairs.",
    "How does all-electronic tolling work?": "All-electronic tolling is a modern, safer, more efficient toll collection system that eliminates the need for cash and coin payments. Tolls are collected electronically using EZ TAGs or by capturing license plate images and billing the vehicle owner.",
    "What happens if I drive through a tolling point without an EZ TAG?": "If you drive through a tolling point without an EZ TAG, your license plate will be photographed, and a bill will be mailed to the vehicle's registered owner.",
    "How do I pay a toll violation?": "Toll violations can be paid online, by mail, or in person at any EZ TAG Store. Please refer to the violation notice for detailed instructions.",
    "What are the hours of operation for the EZ TAG Customer Service Center?": "The EZ TAG Customer Service Center is open Monday through Friday from 8:00 AM to 4:30 PM.",
    "Can I use my EZ TAG on rental cars?": "Yes, you can use your EZ TAG on rental cars. However, you need to add the rental car's license plate to your EZ TAG account temporarily.",
    "How do I update my vehicle information?": "You can update your vehicle information by logging into your EZ TAG account online and making the necessary changes.",
    "What should I do if I sell my car?": "If you sell your car, remove the vehicle from your EZ TAG account and either transfer the EZ TAG to your new vehicle or return it to the EZ TAG Customer Service Center.",
    "How do I replace a lost or damaged EZ TAG?": "To replace a lost or damaged EZ TAG, log into your account online or contact the EZ TAG Customer Service Center. A replacement fee may apply.",
    "Can I have multiple vehicles on one EZ TAG account?": "Yes, you can have multiple vehicles on one EZ TAG account. Each vehicle will need its own EZ TAG.",
    "How do I close my EZ TAG account?": "To close your EZ TAG account, contact the EZ TAG Customer Service Center. Any remaining balance will be refunded to you.",
    "What is the minimum balance required for an EZ TAG account?": "The minimum balance required for an EZ TAG account depends on the number of vehicles and usage frequency. It is typically set to cover at least one month's worth of tolls.",
    "Are there any discounts for frequent toll users?": "Yes, there are discounts for frequent toll users. Details about discount programs can be found on the HCTRA website or by contacting the EZ TAG Customer Service Center.",
    "How do I dispute a toll charge?": "To dispute a toll charge, contact the EZ TAG Customer Service Center with your account details and the reason for the dispute. They will investigate and resolve the issue.",
    "What happens if I don't pay my tolls?": "If you don't pay your tolls, you may receive violation notices, and your account could be referred to a collection agency. Additional fees and penalties may apply.",
    "Can I use my EZ TAG in other states?": "EZ TAG is part of the interoperability network, allowing you to use your tag in several other states. Check the HCTRA website for a list of participating toll agencies.",
    "How do I add funds to my EZ TAG account?": "You can add funds to your EZ TAG account online, by phone, or in person at any EZ TAG Store. Automatic replenishment options are also available.",
    "What is the difference between EZ TAG and EZ TAG Express?": "EZ TAG is a standard transponder-based account, while EZ TAG Express is a credit card-based account that doesn't require a transponder. EZ TAG offers more features and flexibility.",
    "How do I get an EZ TAG?": "You can get an EZ TAG by signing up online or visiting an EZ TAG Store. You will need to provide vehicle and payment information.",
    "What toll roads can I use with my EZ TAG?": "Your EZ TAG can be used on all toll roads operated by HCTRA and other participating toll agencies as part of the interoperability network.",
    "How do I transfer my EZ TAG to a new vehicle?": "To transfer your EZ TAG to a new vehicle, update your vehicle information online or contact the EZ TAG Customer Service Center.",
    "Can I use my EZ TAG on a motorcycle?": "Yes, you can use your EZ TAG on a motorcycle. Make sure to properly secure the tag to your motorcycle according to the instructions provided.",
    "What if I accidentally damage my EZ TAG?": "If you accidentally damage your EZ TAG, contact the EZ TAG Customer Service Center for a replacement. A replacement fee may apply.",
    "Can I get a receipt for my toll transactions?": "Yes, you can get a receipt for your toll transactions by logging into your EZ TAG account online and accessing your transaction history.",
    "How do I set up automatic replenishment?": "You can set up automatic replenishment by logging into your EZ TAG account online and selecting the automatic replenishment option under payment settings.",
    "What payment methods are accepted for EZ TAG accounts?": "Accepted payment methods for EZ TAG accounts include credit cards, debit cards, and electronic checks. Cash payments are accepted at EZ TAG Stores.",
    "How do I change my account password?": "You can change your account password by logging into your EZ TAG account online and selecting the account settings option.",
    "How long does it take to receive my EZ TAG?": "It typically takes 5-7 business days to receive your EZ TAG by mail after your account is activated.",
    "What do I do if I don't receive my EZ TAG?": "If you don't receive your EZ TAG within the expected timeframe, contact the EZ TAG Customer Service Center for assistance.",
    "Can I use my EZ TAG on a trailer or RV?": "Yes, you can use your EZ TAG on a trailer or RV. Make sure to add the trailer or RV to your account and properly install the tag.",
    "How do I check my account balance?": "You can check your account balance by logging into your EZ TAG account online or using the mobile app.",
    "What should I do if my EZ TAG is not working?": "If your EZ TAG is not working, check the installation and contact the EZ TAG Customer Service Center for troubleshooting and replacement options.",
    "Can I get a refund if I close my account?": "Yes, you can get a refund of any remaining balance when you close your EZ TAG account. Contact the Customer Service Center for details.",
    "How do I update my contact information?": "You can update your contact information by logging into your EZ TAG account online and editing your profile details.",
    "What are the benefits of using EZ TAG?": "Benefits of using EZ TAG include convenience, discounted toll rates, and the ability to use toll roads without stopping to pay.",
    "Is there a monthly fee for EZ TAG?": "There is no monthly fee for EZ TAG. However, a minimum balance is required to keep the account active.",
    "Can I pay my tolls with cash?": "Cash payments are not accepted on all-electronic toll roads. You need an EZ TAG or will be billed via Pay By Mail.",
    "How do I contact the EZ TAG Customer Service Center?": "You can contact the EZ TAG Customer Service Center by phone, email, or visiting an EZ TAG Store. Contact details are available on the HCTRA website.",
    "What is the difference between toll roads and regular roads?": "Toll roads require payment for usage and often offer faster, more direct routes compared to regular roads, which are funded by taxes.",
    "Are there any penalties for using a toll road without paying?": "Yes, penalties for using a toll road without paying can include fines, fees, and referral to a collection agency.",
    "How do I sign up for an EZ TAG account?": "You can sign up for an EZ TAG account online or by visiting an EZ TAG Store. You will need to provide vehicle and payment information.",
    "Can I view my toll transactions online?": "Yes, you can view your toll transactions online by logging into your EZ TAG account.",
    "How do I know if my EZ TAG is working?": "You will know your EZ TAG is working if you pass through tolling points without issues and your account shows the transactions.",
    "What is Pay By Mail?": "Pay By Mail is a tolling option where a bill is mailed to the vehicle's registered owner based on license plate images captured at tolling points.",
    "Can I have both an EZ TAG and Pay By Mail account?": "No, you cannot have both an EZ TAG and Pay By Mail account for the same vehicle.",
    "How do I add or remove a vehicle from my account?": "You can add or remove a vehicle from your account by logging into your EZ TAG account online and updating your vehicle information.",
    "What if I have a rental vehicle?": "For rental vehicles, you can temporarily add the rental vehicle's license plate to your EZ TAG account.",
    "How do I update my payment information?": "You can update your payment information by logging into your EZ TAG account online and editing your payment details.",
    "Can I use my EZ TAG in multiple vehicles?": "Each vehicle must have its own EZ TAG. However, multiple vehicles can be managed under one EZ TAG account.",
    "How are toll rates determined?": "Toll rates are determined based on factors such as the cost of road construction and maintenance, traffic volume, and funding needs.",
    "Are there any toll discounts for veterans?": "Yes, certain veterans may qualify for toll discounts. Check the HCTRA website or contact the Customer Service Center for more details.",
    "What should I do if I receive a violation notice in error?": "If you receive a violation notice in error, contact the EZ TAG Customer Service Center to dispute the notice and provide any necessary documentation.",
    "How do I manage my account online?": "You can manage your account online by logging into your EZ TAG account, where you can update information, view transactions, and add funds.",
    "What is the processing fee for Pay By Mail?": "The processing fee for Pay By Mail is included in the total amount due on the bill you receive. Refer to the bill for the exact fee.",
    "Can I use my EZ TAG in other countries?": "Currently, EZ TAG is not accepted in other countries. It is only valid on participating toll roads within the United States.",
    "What if my EZ TAG is stolen?": "If your EZ TAG is stolen, report it immediately to the EZ TAG Customer Service Center and request a replacement. A replacement fee may apply.",
    "How do I get help with my account?": "For help with your account, contact the EZ TAG Customer Service Center by phone, email, or in person at an EZ TAG Store.",
    "What is the refund policy for EZ TAG?": "Refunds for EZ TAG accounts are issued for any remaining balance when you close your account. Contact the Customer Service Center for details.",
    "Can I use my EZ TAG on toll roads in Mexico?": "No, EZ TAG is not valid on toll roads in Mexico. It is only accepted on participating toll roads in the United States.",
    "What happens if I don't have enough funds in my EZ TAG account?": "If you don't have enough funds in your EZ TAG account, you may receive a violation notice or your account could be suspended until sufficient funds are added.",
    "How do I reactivate a suspended account?": "To reactivate a suspended account, add sufficient funds to meet the minimum balance requirement and contact the EZ TAG Customer Service Center if needed.",
    "Can I link my EZ TAG account to multiple payment methods?": "You can link your EZ TAG account to one primary payment method for automatic replenishment. Additional payment methods can be used for manual payments.",
    "What should I do if I receive a toll bill for a vehicle I no longer own?": "If you receive a toll bill for a vehicle you no longer own, contact the EZ TAG Customer Service Center and provide proof of the vehicle's sale or transfer.",
    "Are there any special programs for low-income drivers?": "HCTRA may offer special programs or discounts for low-income drivers. Check the HCTRA website or contact the Customer Service Center for more information.",
    "What are the terms and conditions for using EZ TAG?": "The terms and conditions for using EZ TAG are outlined in the EZ TAG Agreement, which is available on the HCTRA website or by contacting the Customer Service Center.",
    "Can I set spending limits on my EZ TAG account?": "You can manage your account balance and set up notifications for low balance, but specific spending limits cannot be set on an EZ TAG account.",
    "What should I do if my EZ TAG is not detected at a tolling point?": "If your EZ TAG is not detected at a tolling point, ensure it is properly installed and contact the EZ TAG Customer Service Center for assistance.",
    "How do I sign up for electronic statements?": "You can sign up for electronic statements by logging into your EZ TAG account online and selecting the option for electronic statements under account settings.",
    "What is the grace period for paying a toll bill?": "The grace period for paying a toll bill varies. Refer to the due date on the bill or contact the EZ TAG Customer Service Center for specific details.",
    "Can I use my EZ TAG for parking?": "EZ TAG can be used for toll road payments only and is not valid for parking payments.",
    "How do I update my license plate number?": "You can update your license plate number by logging into your EZ TAG account online and editing your vehicle information.",
    "Can I get an EZ TAG for a commercial vehicle?": "Yes, EZ TAGs are available for commercial vehicles. You can sign up for a commercial account online or by visiting an EZ TAG Store.",
    "What if I don't have an EZ TAG and need to use a toll road?": "If you don't have an EZ TAG, you can use the Pay By Mail option, where a bill will be mailed to the vehicle's registered owner based on license plate images.",
    "Are there any benefits for using an EZ TAG over Pay By Mail?": "Benefits of using EZ TAG over Pay By Mail include discounted toll rates, convenience, and avoiding processing fees associated with Pay By Mail.",
    "What should I do if I receive multiple toll bills for the same trip?": "If you receive multiple toll bills for the same trip, contact the EZ TAG Customer Service Center to resolve the issue and ensure accurate billing.",
    "Can I transfer my EZ TAG to another person?": "No, EZ TAGs are non-transferable and should not be transferred to another person. Each user should have their own account and tag.",
    "How do I cancel a payment?": "To cancel a payment, contact the EZ TAG Customer Service Center as soon as possible. Cancellations may not be possible once the payment is processed.",
    "What is the cost of a replacement EZ TAG?": "The cost of a replacement EZ TAG varies. Contact the EZ TAG Customer Service Center for the current replacement fee.",
    "Can I use my EZ TAG for carpools?": "EZ TAG can be used for toll payments in vehicles with multiple occupants, but there are no specific carpool discounts available with EZ TAG.",
    "How do I remove a vehicle from my account?": "You can remove a vehicle from your account by logging into your EZ TAG account online and deleting the vehicle from your account.",
    "Can I use my EZ TAG on a rental RV?": "Yes, you can use your EZ TAG on a rental RV. Be sure to add the rental RV's license plate to your account temporarily.",
    "What happens if I forget to add a rental vehicle to my account?": "If you forget to add a rental vehicle to your account, you may receive a toll bill via Pay By Mail for any tolls incurred while driving the rental vehicle.",
    "Are there any additional fees for using EZ TAG?": "There are no additional fees for using EZ TAG beyond the toll charges and any applicable account maintenance fees.",
    "How do I opt out of receiving paper statements?": "You can opt out of receiving paper statements by logging into your EZ TAG account online and selecting the option for electronic statements.",
    "What if my account is overcharged?": "If your account is overcharged, contact the EZ TAG Customer Service Center to dispute the charge and request a refund if applicable.",
    "Can I use my EZ TAG on toll bridges?": "Yes, EZ TAG can be used on participating toll bridges that accept electronic toll payments.",
    "How do I enroll in automatic replenishment?": "You can enroll in automatic replenishment by logging into your EZ TAG account online and selecting the automatic replenishment option under payment settings.",
    "What if I receive a toll bill for a vehicle I no longer own?": "If you receive a toll bill for a vehicle you no longer own, contact the EZ TAG Customer Service Center and provide proof of the vehicle's sale or transfer.",
    "Are there any special programs for low-income drivers?": "HCTRA may offer special programs or discounts for low-income drivers. Check the HCTRA website or contact the Customer Service Center for more information.",
    "What are the terms and conditions for using EZ TAG?": "The terms and conditions for using EZ TAG are outlined in the EZ TAG Agreement, which is available on the HCTRA website or by contacting the Customer Service Center.",
    "Can I set spending limits on my EZ TAG account?": "You can manage your account balance and set up notifications for low balance, but specific spending limits cannot be set on an EZ TAG account.",
    "What should I do if my EZ TAG is not detected at a tolling point?": "If your EZ TAG is not detected at a tolling point, ensure it is properly installed and contact the EZ TAG Customer Service Center for assistance.",
    "How do I sign up for electronic statements?": "You can sign up for electronic statements by logging into your EZ TAG account online and selecting the option for electronic statements under account settings.",
    "What is the grace period for paying a toll bill?": "The grace period for paying a toll bill varies. Refer to the due date on the bill or contact the EZ TAG Customer Service Center for specific details.",
    "Can I use my EZ TAG for parking?": "EZ TAG can be used for toll road payments only and is not valid for parking payments.",
    "How do I update my license plate number?": "You can update your license plate number by logging into your EZ TAG account online and editing your vehicle information.",
    "Can I get an EZ TAG for a commercial vehicle?": "Yes, EZ TAGs are available for commercial vehicles. You can sign up for a commercial account online or by visiting an EZ TAG Store.",
    "What if I don't have an EZ TAG and need to use a toll road?": "If you don't have an EZ TAG, you can use the Pay By Mail option, where a bill will be mailed to the vehicle's registered owner based on license plate images.",
    "Are there any benefits for using an EZ TAG over Pay By Mail?": "Benefits of using EZ TAG over Pay By Mail include discounted toll rates, convenience, and avoiding processing fees associated with Pay By Mail.",
    "What should I do if I receive multiple toll bills for the same trip?": "If you receive multiple toll bills for the same trip, contact the EZ TAG Customer Service Center to resolve the issue and ensure accurate billing.",
    "Can I transfer my EZ TAG to another person?": "No, EZ TAGs are non-transferable and should not be transferred to another person. Each user should have their own account and tag.",
    "How do I cancel a payment?": "To cancel a payment, contact the EZ TAG Customer Service Center as soon as possible. Cancellations may not be possible once the payment is processed.",
    "What is the cost of a replacement EZ TAG?": "The cost of a replacement EZ TAG varies. Contact the EZ TAG Customer Service Center for the current replacement fee.",
    "Can I use my EZ TAG for carpools?": "EZ TAG can be used for toll payments in vehicles with multiple occupants, but there are no specific carpool discounts available with EZ TAG.",
    "How do I remove a vehicle from my account?": "You can remove a vehicle from your account by logging into your EZ TAG account online and deleting the vehicle from your account.",
    "Can I use my EZ TAG on a rental RV?": "Yes, you can use your EZ TAG on a rental RV. Be sure to add the rental RV's license plate to your account temporarily.",
    "What happens if I forget to add a rental vehicle to my account?": "If you forget to add a rental vehicle to your account, you may receive a toll bill via Pay By Mail for any tolls incurred while driving the rental vehicle.",
    "Are there any additional fees for using EZ TAG?": "There are no additional fees for using EZ TAG beyond the toll charges and any applicable account maintenance fees.",
    "How do I opt out of receiving paper statements?": "You can opt out of receiving paper statements by logging into your EZ TAG account online and selecting the option for electronic statements.",
    "What if my account is overcharged?": "If your account is overcharged, contact the EZ TAG Customer Service Center to dispute the charge and request a refund if applicable.",
    "Can I use my EZ TAG on toll bridges?": "Yes, EZ TAG can be used on participating toll bridges that accept electronic toll payments.",
    "How do I enroll in automatic replenishment?": "You can enroll in automatic replenishment by logging into your EZ TAG account online and selecting the automatic replenishment option under payment settings.",
    "What if I receive a toll bill for a vehicle I no longer own?": "If you receive a toll bill for a vehicle you no longer own, contact the EZ TAG Customer Service Center and provide proof of the vehicle's sale or transfer.",
    "Are there any special programs for low-income drivers?": "HCTRA may offer special programs or discounts for low-income drivers. Check the HCTRA website or contact the Customer Service Center for more information.",
    "What are the terms and conditions for using EZ TAG?": "The terms and conditions for using EZ TAG are outlined in the EZ TAG Agreement, which is available on the HCTRA website or by contacting the Customer Service Center.",
    "Can I set spending limits on my EZ TAG account?": "You can manage your account balance and set up notifications for low balance, but specific spending limits cannot be set on an EZ TAG account.",
    "What should I do if my EZ TAG is not detected at a tolling point?": "If your EZ TAG is not detected at a tolling point, ensure it is properly installed and contact the EZ TAG Customer Service Center for assistance.",
    "How do I sign up for electronic statements?": "You can sign up for electronic statements by logging into your EZ TAG account online and selecting the option for electronic statements under account settings.",
    "What is the grace period for paying a toll bill?": "The grace period for paying a toll bill varies. Refer to the due date on the bill or contact the EZ TAG Customer Service Center for specific details.",
    "Can I use my EZ TAG for parking?": "EZ TAG can be used for toll road payments only and is not valid for parking payments.",
    "How do I update my license plate number?": "You can update your license plate number by logging into your EZ TAG account online and editing your vehicle information.",
    "Can I get an EZ TAG for a commercial vehicle?": "Yes, EZ TAGs are available for commercial vehicles. You can sign up for a commercial account online or by visiting an EZ TAG Store.",
    "What if I don't have an EZ TAG and need to use a toll road?": "If you don't have an EZ TAG, you can use the Pay By Mail option, where a bill will be mailed to the vehicle's registered owner based on license plate images.",
    "Are there any benefits for using an EZ TAG over Pay By Mail?": "Benefits of using EZ TAG over Pay By Mail include discounted toll rates, convenience, and avoiding processing fees associated with Pay By Mail.",
    "What should I do if I receive multiple toll bills for the same trip?": "If you receive multiple toll bills for the same trip, contact the EZ TAG Customer Service Center to resolve the issue and ensure accurate billing.",
    "Can I transfer my EZ TAG to another person?": "No, EZ TAGs are non-transferable and should not be transferred to another person. Each user should have their own account and tag.",
    "How do I cancel a payment?": "To cancel a payment, contact the EZ TAG Customer Service Center as soon as possible. Cancellations may not be possible once the payment is processed.",
    "What is the cost of a replacement EZ TAG?": "The cost of a replacement EZ TAG varies. Contact the EZ TAG Customer Service Center for the current replacement fee.",
    "Can I use my EZ TAG for carpools?": "EZ TAG can be used for toll payments in vehicles with multiple occupants, but there are no specific carpool discounts available with EZ TAG.",
    "How do I remove a vehicle from my account?": "You can remove a vehicle from your account by logging into your EZ TAG account online and deleting the vehicle from your account.",
    "Can I use my EZ TAG on a rental RV?": "Yes, you can use your EZ TAG on a rental RV. Be sure to add the rental RV's license plate to your account temporarily.",
    "What happens if I forget to add a rental vehicle to my account?": "If you forget to add a rental vehicle to your account, you may receive a toll bill via Pay By Mail for any tolls incurred while driving the rental vehicle.",
    "Are there any additional fees for using EZ TAG?": "There are no additional fees for using EZ TAG beyond the toll charges and any applicable account maintenance fees.",
    "How do I opt out of receiving paper statements?": "You can opt out of receiving paper statements by logging into your EZ TAG account online and selecting the option for electronic statements.",
    "What if my account is overcharged?": "If your account is overcharged, contact the EZ TAG Customer Service Center to dispute the charge and request a refund if applicable.",
    "Can I use my EZ TAG on toll bridges?": "Yes, EZ TAG can be used on participating toll bridges that accept electronic toll payments.",
    "How do I enroll in automatic replenishment?": "You can enroll in automatic replenishment by logging into your EZ TAG account online and selecting the automatic replenishment option under payment settings.",
    "What if I receive a toll bill for a vehicle I no longer own?": "If you receive a toll bill for a vehicle you no longer own, contact the EZ TAG Customer Service Center and provide proof of the vehicle's sale or transfer.",
    "Are there any special programs for low-income drivers?": "HCTRA may offer special programs or discounts for low-income drivers. Check the HCTRA website or contact the Customer Service Center for more information.",
    "What are the terms and conditions for using EZ TAG?": "The terms and conditions for using EZ TAG are outlined in the EZ TAG Agreement, which is available on the HCTRA website or by contacting the Customer Service Center.",
    "Can I set spending limits on my EZ TAG account?": "You can manage your account balance and set up notifications for low balance, but specific spending limits cannot be set on an EZ TAG account.",
    "What should I do if my EZ TAG is not detected at a tolling point?": "If your EZ TAG is not detected at a tolling point, ensure it is properly installed and contact the EZ TAG Customer Service Center for assistance.",
    "How do I sign up for electronic statements?": "You can sign up for electronic statements by logging into your EZ TAG account online and selecting the option for electronic statements under account settings.",
    "What is the grace period for paying a toll bill?": "The grace period for paying a toll bill varies. Refer to the due date on the bill or contact the EZ TAG Customer Service Center for specific details.",
    "Can I use my EZ TAG for parking?": "EZ TAG can be used for toll road payments only and is not valid for parking payments.",
    "How do I update my license plate number?": "You can update your license plate number by logging into your EZ TAG account online and editing your vehicle information.",
    "Can I get an EZ TAG for a commercial vehicle?": "Yes, EZ TAGs are available for commercial vehicles. You can sign up for a commercial account online or by visiting an EZ TAG Store.",
    "What if I don't have an EZ TAG and need to use a toll road?": "If you don't have an EZ TAG, you can use the Pay By Mail option, where a bill will be mailed to the vehicle's registered owner based on license plate images.",
    "Are there any benefits for using an EZ TAG over Pay By Mail?": "Benefits of using EZ TAG over Pay By Mail include discounted toll rates, convenience, and avoiding processing fees associated with Pay By Mail.",
    "What should I do if I receive multiple toll bills for the same trip?": "If you receive multiple toll bills for the same trip, contact the EZ TAG Customer Service Center to resolve the issue and ensure accurate billing.",
    "Can I transfer my EZ TAG to another person?": "No, EZ TAGs are non-transferable and should not be transferred to another person. Each user should have their own account and tag.",
    "How do I cancel a payment?": "To cancel a payment, contact the EZ TAG Customer Service Center as soon as possible. Cancellations may not be possible once the payment is processed.",
    "What is the cost of a replacement EZ TAG?": "The cost of a replacement EZ TAG varies. Contact the EZ TAG Customer Service Center for the current replacement fee.",
    "Can I use my EZ TAG for carpools?": "EZ TAG can be used for toll payments in vehicles with multiple occupants, but there are no specific carpool discounts available with EZ TAG.",
    "How do I remove a vehicle from my account?": "You can remove a vehicle from your account by logging into your EZ TAG account online and deleting the vehicle from your account.",
    "Can I use my EZ TAG on a rental RV?": "Yes, you can use your EZ TAG on a rental RV. Be sure to add the rental RV's license plate to your account temporarily.",
    "What happens if I forget to add a rental vehicle to my account?": "If you forget to add a rental vehicle to your account, you may receive a toll bill via Pay By Mail for any tolls incurred while driving the rental vehicle.",
    "Are there any additional fees for using EZ TAG?": "There are no additional fees for using EZ TAG beyond the toll charges and any applicable account maintenance fees.",
    "How do I opt out of receiving paper statements?": "You can opt out of receiving paper statements by logging into your EZ TAG account online and selecting the option for electronic statements.",
    "What if my account is overcharged?": "If your account is overcharged, contact the EZ TAG Customer Service Center to dispute the charge and request a refund if applicable.",
    "Can I use my EZ TAG on toll bridges?": "Yes, EZ TAG can be used on participating toll bridges that accept electronic toll payments.",
    "How do I enroll in automatic replenishment?": "You can enroll in automatic replenishment by logging into your EZ TAG account online and selecting the automatic replenishment option under payment settings.",
    "What if I receive a toll bill for a vehicle I no longer own?": "If you receive a toll bill for a vehicle you no longer own, contact the EZ TAG Customer Service Center and provide proof of the vehicle's sale or transfer.",
    "Are there any special programs for low-income drivers?": "HCTRA may offer special programs or discounts for low-income drivers. Check the HCTRA website or contact the Customer Service Center for more information.",
    "What are the terms and conditions for using EZ TAG?": "The terms and conditions for using EZ TAG are outlined in the EZ TAG Agreement, which is available on the HCTRA website or by contacting the Customer Service Center.",
    "Can I set spending limits on my EZ TAG account?": "You can manage your account balance and set up notifications for low balance, but specific spending limits cannot be set on an EZ TAG account.",
    "What should I do if my EZ TAG is not detected at a tolling point?": "If your EZ TAG is not detected at a tolling point, ensure it is properly installed and contact the EZ TAG Customer Service Center for assistance.",
    "How do I sign up for electronic statements?": "You can sign up for electronic statements by logging into your EZ TAG account online and selecting the option for electronic statements under account settings.",
    "What is the grace period for paying a toll bill?": "The grace period for paying a toll bill varies. Refer to the due date on the bill or contact the EZ TAG Customer Service Center for specific details.",
    "Can I use my EZ TAG for parking?": "EZ TAG can be used for toll road payments only and is not valid for parking payments.",
    "How do I update my license plate number?": "You can update your license plate number by logging into your EZ TAG account online and editing your vehicle information.",
    "Can I get an EZ TAG for a commercial vehicle?": "Yes, EZ TAGs are available for commercial vehicles. You can sign up for a commercial account online or by visiting an EZ TAG Store.",
    "What if I don't have an EZ TAG and need to use a toll road?": "If you don't have an EZ TAG, you can use the Pay By Mail option, where a bill will be mailed to the vehicle's registered owner based on license plate images.",
    "Are there any benefits for using an EZ TAG over Pay By Mail?": "Benefits of using EZ TAG over Pay By Mail include discounted toll rates, convenience, and avoiding processing fees associated with Pay By Mail.",
    "What should I do if I receive multiple toll bills for the same trip?": "If you receive multiple toll bills for the same trip, contact the EZ TAG Customer Service Center to resolve the issue and ensure accurate billing.",
    "Can I transfer my EZ TAG to another person?": "No, EZ TAGs are non-transferable and should not be transferred to another person. Each user should have their own account and tag.",
    "How do I cancel a payment?": "To cancel a payment, contact the EZ TAG Customer Service Center as soon as possible. Cancellations may not be possible once the payment is processed.",
    "What is the cost of a replacement EZ TAG?": "The cost of a replacement EZ TAG varies. Contact the EZ TAG Customer Service Center for the current replacement fee.",
    "Can I use my EZ TAG for carpools?": "EZ TAG can be used for toll payments in vehicles with multiple occupants, but there are no specific carpool discounts available with EZ TAG.",
    "How do I remove a vehicle from my account?": "You can remove a vehicle from your account by logging into your EZ TAG account online and deleting the vehicle from your account.",
    "Can I use my EZ TAG on a rental RV?": "Yes, you can use your EZ TAG on a rental RV. Be sure to add the rental RV's license plate to your account temporarily.",
    "What happens if I forget to add a rental vehicle to my account?": "If you forget to add a rental vehicle to your account, you may receive a toll bill via Pay By Mail for any tolls incurred while driving the rental vehicle.",
    "Are there any additional fees for using EZ TAG?": "There are no additional fees for using EZ TAG beyond the toll charges and any applicable account maintenance fees.",
    "How do I opt out of receiving paper statements?": "You can opt out of receiving paper statements by logging into your EZ TAG account online and selecting the option for electronic statements.",
    "What if my account is overcharged?": "If your account is overcharged, contact the EZ TAG Customer Service Center to dispute the charge and request a refund if applicable.",
    "Can I use my EZ TAG on toll bridges?": "Yes, EZ TAG can be used on participating toll bridges that accept electronic toll payments.",
    "How do I enroll in automatic replenishment?": "You can enroll in automatic replenishment by logging into your EZ TAG account online and selecting the automatic replenishment option under payment settings."
}

# Call List
call_list = {
    "Human Resources": {
        "Dimitri, Johanna": "7633",
        "Ecklin, Deborah": "7801",
        "Duran, Janet M.": "7877",
        "Morrissey, Tracy": "7606",
        "Mangum, Alexandria": "7848",
        "Quinn, Ambal": "7793",
        "Anderson, Rick": "7810",
        "Carbajal, Ashley": "7944",
        "Coleman, Al": "7640",
        "Hernandez, Natalia L.": "7997",
        "Manzanares, Max": "7973",
        "Upward, Noah": "7794",
        "Macias, Jalisa": "7844",
        "Gatlin, LaWana": "7903",
        "Ayar, Rebecca": "7147",
        "Perez, Laura": "7721",
        "Salazar-Perez, Cecilia": "7836",
        "Houston, Taylor": "7792",
        "Payroll/Benefits": "7962"
    },
    "Project Controls": {
        "Ahmed, Taha": "7649",
        "Rubio, Melina": "7685",
        "Corrigeux, Caleb": "7623"
    },
    "Budget & Financial Analysis": {
        "Jernagin, Shaun": "7670",
        "Chamroeun, Nancy": "7819",
        "Le, Kevin": "7882",
        "Meek, Rosalba": "7672",
        "Nguyen, Mary": "7634",
        "Guerrero, Alexis": "7156",
        "Ha, Chau": "7163",
        "Nguyen, Thomas": "7752",
        "Flores, Evelyn": "7928"
    },
    "Communications / GIS": {
        "Jackson, Tracy": "7763",
        "Martinez, Michael": "7616",
        "Wood, Marlena": "7625",
        "Cowart, Jason": "7884",
        "Chavez, Angelica": "7883",
        "Kons, Holly": "7405",
        "Brown, Sharayne": "7129",
        "Joffrion, Christopher": "7627",
        "DeSilva, Kumudu": "7148",
        "Argento, Joshua": "7692",
        "Darby, David": "7664",
        "Linsey, Shaun": "7157",
        "Orr, Joshua": "7859",
        "Walker, Jennifer": "7126",
        "Hernandez, Eusebio": "7118",
        "Ernstrom, Hyrum": "7136",
        "Lozano, Theresa": "7696",
        "Hardy DWTN Connector": "6001"
    },
    "Administrative Services": {
        "Hamilton, Emerill": "7618"
    },
    "Records Management": {
        "Allen, Kelly": "7818",
        "Griffin, Jacqueline": "7823",
        "Harris, LaKay": "7817",
        "Lopez, Cinthya": "7834",
        "Nguyen, Teri": "7869",
        "Peevy, Carla": "7800",
        "Jefferson, JoAnn": "7994",
        "Ayala, Jose": "7846",
        "Moreno, Albert": "7846",
        "Supply Room": "7146"
    },
    "Inventory Management": {
        "Frazier, Jason": "(832) 590-6931",
        "Pore, Tricia": "(832) 590-6984",
        "Torres, Ricardo": "(832) 590-6937",
        "Montalbano, James": "(832) 590-6933",
        "Osteen, Seth": "(832) 590-6966"
    },
    "Fleet Management": {
        "Brown, Brandon": "7526"
    },
    "Process Review": {
        "Beck, Tammy": "7828",
        "Mullen, Glen": "7527",
        "Richardson, Robin": "7762",
        "Brinkmeyer, Michelle": "7872",
        "Brooks, Canarika": "7170",
        "Brown, Robert": "7124",
        "Henry, Gwendolyn": "7790",
        "Ramos, Maria": "7914",
        "Reece, Sherrie": "7605"
    },
    "Facilities Management": {
        "Building Facilities": "7970",
        "Bouse, Emma": "7979",
        "Brown, Waylon": "7915",
        "Martin, Robert": "7881",
        "Beaudoin, Pemilia": "7992",
        "Harris, Deonechia": "7970",
        "Anderson, Heather": "7970",
        "Jones, Cynthia": "7970",
        "Seltzer, David": "7970",
        "Varnado, Archie": "7970",
        "Anderson, Daniel": "7970",
        "Collins, Afrose": "7970",
        "Jones, Linda": "7970",
        "Reddix, Minyard": "7970",
        "Rodela, Jimmy": "7970",
        "Nguyen, Joshua": "7970",
        "Ayala, Guadalupe": "7970",
        "Phan, Brandon": "7970",
        "Aguirre, Leonor": "7970",
        "Simon, Linda": "7970",
        "Abdulovic, Biljana": "7970",
        "Clay, Sheila": "7970",
        "Randle, Terence": "7970",
        "Sessum, Eloisa": "7970",
        "Titus, Mollie": "7970",
        "Van, Hung": "7970",
        "Velasquez, Alberto": "7970",
        "Velasquez, Edith": "7970",
        "Wells, Kimberly": "7970",
        "Evans, Shampale": "7970",
        "Garrett, Sharon": "7970",
        "Pointer, Dionna": "7970",
        "Salazar, Liliana": "7970",
        "Draughon, Phillip": "7970",
        "Williams, Jason": "7970"
     },
    "Supply Chain Management": {
        "Willingham, Bernard": "7653",
        "Gibson, Tara": "7402"
    },
    "Procurement": {
        "Hubbard, Benard \"BJ\", J.D.": "7638",
        "Arredondo, Sue Ellen": "7797",
        "Cormier, Bridget": "7109",
        "Williams, Shadonna": "7505"
    },
    "Contract Administration / Accounts Payable": {
        "Barrett, Desiree": "7885"
    },
    "Contract Administration": {
        "Austin, Marisela": "7919",
        "Suarez, Doris": "7657",
        "Clark, Kendra": "7120",
        "Melancon, Allaina": "7945",
        "Minter, Roberta": "7671",
        "Ortiz, Hristo": "7625",
        "Ramirez, Anamaria": "7403",
        "Rangel, Monica": "7119",
        "York, Princess": "7659"
    },
    "Accounts Payable": {
        "McAdoo, Timothy": "7631",
        "Ellis, Eddie": "7617",
        "Holmes, Lanita": "7993",
        "Garcia, Percill": "7675",
        "Gold, Sharon": "7875",
        "Howard, Michell": "7764",
        "Kohanski, Carol": "7933"
     },
    "Engineering": {
        "Qumruzzaman, Mohammed": "7864",
        "Leija, Arnulfo (Nuco)": "(832) 623-8500",
        "Tamayo, Adrian": "(832) 434-7573",
        "Marksberry, Penny": "7729"
    },
    "Ship Channel Bridge Program": {
        "Oviedo, Omar": "7926"
    },
    "Sustainability & Reliance": {
        "Abraham, Dr. David": "7400"
    },
    "Traffic Operations & ITS": {
        "Carroll, Christopher": "7809",
        "Fearon, David": "7841",
        "Jasso, Sergio": "7149",
        "Mendez, Miguel": "7754"
    },
    "Utilities Permit Review": {
        "Kang, Hun": "7171"
    },
    "Project Management": {
        "Mothe, Ram": "7698",
        "Griffith, Dara": "7140",
        "Guerra, Victoria": "7107",
        "Emery, Doug": "7968",
        "Sterling, Kaleb": "7894",
        "Givens, Patrick": "(713) 992-1948",
        "Quiroga, Henry": "(281) 224-6305",
        "Huynh, San": "7796",
        "McKenzie, Michael": "(713) 409-1275",
        "Sureja, Girish": "(713) 873-1210",
        "Kelekci, Mehmet \"Matt\"": "(713) 269-8936"
    },
    "Roadway & Facility Infrastructure Maintenance": {
        "Griffin, Wendell": "7756",
        "Murphy, Sandy": "(832) 590-6936",
        "Peterson, Rivers": "(281) 543-9924",
        "Montalbano, Michael": "(281) 455-8917",
        "Niver, Donald": "(832) 860-3557",
        "Breaux, Louis": "(713) 594-7056",
        "Harless, Samuel": "(281) 467-0183",
        "Mendiola, Richard": "(713) 280-6083",
        "Castro, Simon": "(281) 732-1406",
        "Ferguson, Jimmiesue": "(832) 365-9040",
        "Fowler, Jackie": "(832) 641-7838",
        "Gatewood, Rick": "(281) 380-2528",
        "Hernandez, Jonathan": "(832) 766-6522",
        "Jones, Darius": "(832) 887-0072",
        "Landor, Jermaine": "(409) 543-5369",
        "Maia, Trevor": "(346) 336-0057",
        "Maggio, Pete": "(832) 291-8514",
        "Martinez, Erick": "(936) 499-5696",
        "Martinez, Daniel": "(203) 306-7071",
        "Machicek, Jason": "(281) 610-8499",
        "Cavazos, Jose": "(832) 367-1855",
        "Jury, Kenneth": "(405) 623-4658"
    },
        "Emergency Management": {
        "Dispatch Center": "(281) 584-7500",
        "Dispatch Lead Desk": "(281) 584-7535",
        "Johnson, Jessica": "(281) 584-7549",
        "Desai, Sagar": "7874",
        "Pasley, Jarett": "7101",
        "Krause, Darrell": "(281) 584-7105",
        "Lopez, Madeline": "7516"
    },
    "IMD - Incident Response": {
        "Bryant, Edwyn": "7948",
        "Ontiveros, Lisa": "7603",
        "Lee, James": "7948",
        "Andrus, Lorenzo": "7948",
        "Kohl, Alex": "7948",
        "Richards, James": "7948",
        "Sherer, Mike": "7948",
        "Smith, Shannon": "7948"
    },
    "Risk Management": {
        "Cossey, Clayton": "7774",
        "Mallery, Theresa": "7811"
    },
    "Safety & Security": {
        "Jasso, Daniel": "7856",
        "Mangum, Cody": "7682"
    },
    "Lynchburg Ferry & Washburn Tunnel": {
        "Hinojosa, Gualberto \"Wally\"": "(713) 983-1887"
    },
    "Lynchburg Ferry": {
        "Foerster, Robbye": "(713) 983-1890",
        "Newsom, Diana": "(713) 983-1886"
    },
    "Washburn Tunnel": {
        "Salazar, John": "(713) 983-1871",
        "Hernandez, Jessica": "(713) 983-1873",
        "Lanphier, Stephen": "(713) 983-1874"
    },
    "Tolling Operations": {
        "Mirmira, Anil": "7614",
        "Black, Norma": "7876"
    },
    "Public Safety & Operations": {
        "Harvey, Calvin": "(281) 584-7502",
        "Green, Jason": "(281) 584-7562",
        "Isom, John": "7515",
        "Eichenour, Chad": "7532 / 7520",
        "Heiman, Angel": "(281) 584-7514",
        "Wilson, Ashley": "7524"
    },
    "Public Safety & Operations": {
        "Harvey, Calvin": "(281) 584-7502",
        "Green, Jason": "(281) 584-7562",
        "Isom, John": "7515",
        "Eichenour, Chad": "7532 / 7520",
        "Heiman, Angel": "(281) 584-7514",
        "Wilson, Ashley": "7524"
    },
     "Administration": {
        "McLemore, Jason": "7401",
        "Luis, Melissa": "7927",
        "Meek, Christopher": "7501",
        "Edgerton, Martha": "7922"
    },
    "Capital Planning": {
        "Mohite, Amar": "7936",
        "Ortiz, Josie": "7680"
    },
        "Executive Office": {
        "Treviño, Roberto": "7177",
        "Stuttz, Nicole": "7615",
        "Santos, Maria": "7978",
        "Linebarger, Marcy": "7971"
    },
        "Barrier Free HCTRA (BFH)": {
        "Castelblanco, Adhara": "7114",
        "Juarez, Monica": "7940",
        "Bessala, Didier": "7871"
    },
    "Project Portfolio Management": {
        "Herman, Dylan": "7761",
        "Hall, Mary": "7879",
        "Hussein, Kyle": "7688"
    },
    "Operations": {
        "White, Courtney": "7142",
        "Wethington, Misty": "7998"
    },
    "Customer Service": {
        "Moreno-Cruz, Jacqueline": "7862",
        "Long, Alison": "7806",
        "Docherty, Karen": "7840",
        "Brown, Denitra": "7850",
        "Dahl, Jonathan": "7755",
        "Hart, Carla": "6826",
        "Mazique, Valerie": "7647",
        "Washington, Tusar": "7151",
        "Thomas, Lauriel": "7128",
        "Rhone Dominique": "(281) 301-6836",
        "Gaines, Neil": "(281) 584-7504",
        "Stokes, Demarcus": "(281) 301-6812"
    },
    "Image Review": {
        "Hazzard-Williams, Cathy": "7831",
        "Whitley, Jan": "7921",
        "Carthen, Marlene": "7849",
        "Bowser, Adrian": "7673",
        "Dominguez, Jesse": "(832) 797-6857",
        "Savoy Jr., Timothy": "7684"
    },
    "Computer Vision Annotation Tool (CVAT) - Fournace": {
        "Savoy Jr., Timothy": "7684",
        "Ganey, Mahogany": "(713) 382-2481"
    },
    "Image Review (IR) - Fournace": {
        "Kearns, Terrance": "(281) 974-8581",
        "Harmer, Megan": "7135"
    },
    "Image Review Audit (IRA) - Federal": {
        "McGautha, Cantrina": "7108",
        "Smith, Gail": "(832) 512-9144"
    },
      "Image Review Audit Validation (IRAV)": {
        "Dominguez, Jesse": "(832) 797-6857"
    },
    "Lane Audit Application (LAA)": {
        "Whitley, Jan": "(713) 628-4149",
        "Sims, Kendrick": "(832) 488-6366"
    },
    "Technology": {
        "Patterson, David": "7613",
        "Espino, Cynthia": "7888"
    },
    "Planning Development Services (PDS)": {
        "Urban, Brad": "7612",
        "Heath, Kelsey": "7918",
        "Leija, Shannon": "7938"
    },
    "IT System Support": {
        "Service Desk - Wilshire": "7911",
        "Aghassi, Edmond": "7960",
        "Gonzalez, Carlos": "7602 / 3990",
        "Diaz, Joey": "7713 / 3537",
        "Garza, Michael": "6886 / 3510",
        "Graddy, Lincoln": "6660 / 3350",
        "Nelson, Brittani": "7000",
        "Plummer, Anthony": "7699"
    },
    "Service Desk - DATS": {
        "Mitchell, Sheron": "7456 / 3345",
        "Voges, Michael": "7896 / 3131"
    },
    "Service Desk - Harris Health / Fournace Call Center": {
        "Wise, Ryan": "7110 / 3090"
    },
    "Service Desk - Hammer": {
        "Chavarria, Isaac": "6680 / 3471"
    },
    "Service Desk - NW 290 / DATS": {
        "Johse, Doug": "7629 / 3070"
    },
    "Service Desk - NW 290": {
        "Buono, Sabrina": "7690 / 3059",
        "Diaz, Jimmy": "7607 / 3217",
        "Cramer, Jordan": "7174 / 3974",
        "Johnson, Joshua": "7763 / 3190",
        "Jones, Tristan": "7112 / 3315",
        "Payne, Collis": "7681 / 3991",
        "Sabong, Ramon": "7868 / 3054"
    },
    "Service Desk - West Tag / Training": {
        "Johnson, Quarry": "6887 / 3401"
    },
    "Organizational Change Management (OCM)": {
        "Traylor, Glenn": "7780",
        "Harang, Jeff": "7942",
        "Hopkins, Martrice": "7860",
        "Rander, Page": "7932",
        "Chessher, Michael": "7663",
        "Tomoye, John": "7771"
    },
    "IT Operations": {
        "Pierce, Mark": "7954"
    },
    "IT Infrastructure": {
        "Frank Sr., Antonio": "7833",
        "Escudero, Jose": "7693",
        "Rivas, Danilo": "7692",
        "Robinson, Paul": "7766"
    },
    "Network": {
        "Hill, Stan": "7880",
        "Gilbert, Mark": "7949",
        "Vidojevic, Zoran": "7611",
        "Martinez, Juan": "(832) 458-7759",
        "Carmona, Emilo": "7697",
        "Renteria, Jose": "7694",
        "Wood, Clinton": "7621"
    },
    "Enterprise Architecture": {
        "Chowdhary, Sanjib": "7679",
        "Qadri, Syed": "7989"
    },
    "UNIX": {
        "Dang, Tuan": "7790",
        "Porras, Andy": "7667",
        "Prendergast, Kevin": "7670",
        "Ngalle, Martha": "(704) 977-7197"
    },
    "Windows": {
        "Murphy, Mike": "7988",
        "Assaad, Ayman 'Hadi'": "7662",
        "Bhuptani, Hemal": "7674",
        "Dean, Kelly": "7952"
    },
    "Cybersecurity & Risk": {
        "Tippey, Tamara": "7972",
        "Harris, Agnes": "7950",
        "Hunt, Frank": "7842",
        "Korone, Geoff": "7786",
        "Davis, Luke": "7909",
        "Lehmann, Ryan": "7622"
    },
        "Tolling Systems": {
        "Bhat, Vasudha": "(757) 469-2665",
        "Martin, Javier": ""
    },
    "Application Management & Governance": {
        "Brown, Anne": "7668",
        "Adams, TJ": "7855",
        "Bennett, Larry": "7610",
        "Henderson, Kimberly": "7405",
        "Loggains, Gary": "7650",
        "Palmquist, Chad": "7824"
    },
    "Product Delivery": {
        "Adzhamova, Milena": "7684",
        "Velasquez, Diane": "7679",
        "Ruiz, Abbigail": "(832) 641-7838",
        "Daniels, Regina": "7000",
        "Hernandez, Peter": "(713) 253-2859",
        "Sustaita Jr., Ray": "7628",
        "Hammad, Mohammad": "7749",
        "Lee, Wilson": "7792",
        "Ramsey, Todd": "7676"
    },
    "Toll Engineering": {
        "Finberg, Ron": "(281) 630-2471",
        "Rodriguez Jr., Charles": "7658",
        "Wethington, Kenneth": "7779"
    },
    "Revenue Accounting": {
        "Griffin, Ken": "7829",
        "Lemmonds, Tammie": "7907",
        "Nelson, Paul": "7886",
        "Tillman, Candance": "7646",
        "Balbuena, Raul": "7130",
        "Cunningham, Cassandra": "7830",
        "Wallace, Marcel": "7687"
    },
    "Project Management Support": {
        "Lagerstrom, Tim": "(713) 397-7638",
        "Lehmann, Ryan": "(832) 221-5228",
        "Liddell, Maurice": "(281) 728-6618",
        "Ngalle, Martha": "(704) 977-7197",
        "Prendergast, Kevin": "(832) 427-9166",
        "Ranjesh, Ganesh": "(608) 358-3582",
        "Smith, Richard \"Darrell\"": "(832) 716-8333",
        "Wright, Dave": "(832) 524-5435",
        "Ahmed, Adeel": "(469) 597-9494",
        "Copeland, Trey": "(713) 906-2105",
        "Eriksen, Chris": "(346) 377-2821",
        "Khan, Asif": "(832) 655-7942",
        "Koleoso, Lola": "(281) 883-3963",
        "Kuppuswamy, Elan": "(469) 500-2556",
        "Nagarwala, Shabbir": "(281) 414-7614",
        "Nkenfaryi, Theo N.": "(281) 900-6950",
        "Oliver, Deborah": "(281) 883-9647",
        "Sarkar, Jayeeta": "(281) 772-6873",
        "Wheldon, Mark": "(832) 693-3669",
        "Cooper, Scott": "(713) 829-3384",
        "Boatman, Susan": "(713) 898-5392",
        "Dean, Kelly": "(832) 414-6975",
        "DiAngelo, David": "(713) 408-4582",
        "Martinez, Juan": "(832) 458-7759",
        "Milligan, Tyler": "(832) 323-3363",
        "St. Andre, Sarah": "(832) 535-5097",
        "Cloutier, Jon": "(513) 297-7727",
        "Jaiparia, Sunny": "(857) 939-1687",
        "TransCore": "(713) 939-5444"
    }
}

def find_response(user_input, category_responses):
    # Tokenize user input into words
    user_words = set(user_input.lower().split())

    best_match = None
    best_score = 0

    # Iterate through keywords and responses
    for keyword, response in category_responses.items():
        keyword_words = set(keyword.lower().split())

        # Calculate the intersection of user words and keyword words
        common_words = user_words.intersection(keyword_words)
        score = len(common_words) / len(keyword_words)  # Simple score based on word overlap

        # Update the best match if current score is higher
        if score > best_score:
            best_score = score
            best_match = response

    # Define a threshold for the matching score (adjust as needed)
    threshold = 0.5
    if best_score >= threshold:
        return best_match
    else:
        return "Sorry, I don't have an answer for that question."

# Cache function for getting department data
@st.cache_data
def get_department_data(department):
    return call_list.get(department, {})

def main():
    # Initialize state variables
    if 'show_chat' not in st.session_state:
        st.session_state.show_chat = False
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'previous_category' not in st.session_state:
        st.session_state.previous_category = None
    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""

    # Display chat interface or welcome message
    if not st.session_state.show_chat:
        st.title("Welcome to the HCTRA Baby Bot")
        st.write("This chatbot is designed to assist you with various queries related to HCTRA. You can ask questions about Procurement and Contracts, Capital and Budget, Operations and Maintenance, Quickbase, or HCTRA-specific topics.")
        if st.button("Start Chat"):
            st.session_state.show_chat = True
            st.experimental_rerun()
    else:
        st.title("HCTRA Chatbot")

        # Category selection
        with st.sidebar:
            st.header("Categories")
            categories = {
                "Procurement and Contracts": procurement_and_contracts,
                "Capital and Budget": capital_and_budget,
                "Operations and Maintenance": operations_and_maintenance,
                "Quickbase": quickbase,
                "HCTRA Specific": hctra_faq,
                "Call List": call_list
            }
            selected_category = st.selectbox("Select a Category", list(categories.keys()))

            # Check if category has changed
            if st.session_state.previous_category != selected_category:
                st.session_state.previous_category = selected_category
                st.session_state.user_input = ""  # Reset user input

            st.session_state.selected_category = selected_category

        # Handling different categories
        if st.session_state.selected_category == "Call List":
            department = st.selectbox("Select a Department", list(call_list.keys()))
            if department:
                department_data = get_department_data(department)
                st.write(f"**Department:** {department}")

                if department_data:
                    person = st.selectbox("Select a Person", list(department_data.keys()))
                    if person:
                        st.write(f"Extension: {department_data[person]}")
                else:
                    st.write("No data available for this department.")
        else:
            # Add button to clear chat history
            if st.button("Clear Chat History"):
                st.session_state.chat_history = []

            # Manually manage text input
            user_input = st.text_input("Type your query here (press 'Send' button to submit):", st.session_state.user_input)

            if st.button("Send"):
                if user_input:
                    st.session_state.chat_history.append(f"You: {user_input}")

                    # Get responses based on the selected category
                    category_responses = categories.get(st.session_state.selected_category, {})
                    bot_response = find_response(user_input, category_responses)

                    st.session_state.chat_history.append(f"Bot: {bot_response}")

                    # Clear text input field
                    st.session_state.user_input = ""

            # Display chat history
            for message in st.session_state.chat_history:
                st.write(message)

if __name__ == "__main__":
    main()