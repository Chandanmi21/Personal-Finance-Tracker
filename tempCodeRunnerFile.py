 CSV.initialize_csv()
    date = get_date("Enter the date of transaction (dd-mm-yyyy) or enter for today's date:" ,
                     allow_default=True,
                     )
    amount = get_amount()
    category = get_category()
    description=get_description()
    CSV.add_entry(date,amount,category,description)