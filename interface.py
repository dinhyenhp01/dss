st.title('Dashboard')
column_1, column_2 = st.beta_columns(2)

with column_1:
    st.header('Save records')
    name = st.text_input('Please enter name')
    details = st.text_input('Please enter details (separated by comma)')
    details = ('{%s}' % (details))
    if st.button('Save record to database'):
        write_record(name,details,engine)
        st.info('Name: **%s** and details: **%s** saved to database' % (name,details[1:-1]))

    st.header('Update records')
    field = st.selectbox('Please select field to update',('name','details'))
    name_key = st.text_input('Please enter name of record to be updated')    
    if field == 'name':
        updated_name = st.text_input('Please enter updated name')
        if st.button('Update records'):
            update_record(field,name_key,updated_name,engine)
            st.info('Updated name to **%s** in record **%s**' % (updated_name,name_key))                
    elif field == 'details':
        updated_details = st.text_input('Please enter updated details (separated by comma)')
        updated_details = ('{%s}' % (updated_details))  
        if st.button('Update records'):
            update_record(field,name_key,updated_details,engine)
            st.info('Updated details to  **%s** in record **%s**' % (updated_details[1:-1],name_key))
            
    st.header('Read records')
    record_to_read = st.text_input('Please enter name of record to read')
    if st.button('Search'):
        read_name = read_record('name',record_to_read,engine)
        read_details = read_record('details',record_to_read,engine)
        st.info('Record name is **%s**, record details is **%s**' % (read_name,str(read_details)[1:-1]))

with column_2:
    st.header('Save datasets')
    dataset = st.file_uploader('Please upload dataset')
    if dataset is not None:
        dataset = pd.read_csv(dataset)
        dataset_name = st.text_input('Please enter name for dataset')
        if st.button('Save dataset to database'):
            write_dataset('%s' % (dataset_name),dataset,engine_dataset)
            st.info('**%s** saved to database' % (dataset_name))

    try:
        read_title = st.empty()
        dataset_to_read = st.selectbox('Please select dataset to read',([x[0] for x in list_datasets(engine_dataset)]))
        read_title.header('Read datasets')
        if st.button('Read dataset'):
            df = read_dataset(dataset_to_read,engine_dataset)
            st.subheader('Chart')
            st.line_chart(df['value'])
            st.subheader('Dataframe')
            st.write(df)    
    except:
        pass
