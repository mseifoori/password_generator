import streamlit as st

from src.main import pin_password_generator, words_password_generator, random_password_generator, memorable_password_generator


st.title('Password Generator Project :closed_lock_with_key:')

password_type = st.selectbox(
    'Choose a password type:',
    ('Pin', 'Words', 'Random', 'Memorable')
)

if password_type == 'Pin':
    length = st.slider('Password legnth:', 8, 16)
    pin_generated_password = pin_password_generator(length)
    user_choice = st.toggle('Do you want to see your password?')
    if user_choice:
        st.success(f'Here is your password: {pin_generated_password})')

elif password_type == 'Words':
    user_vocab_confirmation = st.checkbox('Do you have any words you want to make your password with?')
    if user_vocab_confirmation:
        user_vocab = st.text_input('Please enter your recommended words:\n(min: 4 words):')
        user_vocab = [word.strip() for word in user_vocab.split(',')]
        length = st.slider('Password length (number of words):', 4, 8)
        capitalization = st.checkbox('Should words be capitalaized?')
        seperator = st.text_input('Words are seperated with (for example ","):')
        all_capitalized= st.checkbox('Do you want all the words to be capitalized?')
        
        words_generated_password = words_password_generator(
            length,
            capitalization,
            all_capitalized,
            seperator,
            user_vocab
        )   
        
        user_choice = st.toggle('Do you want to see your generated password?')
        if user_choice:
            st.success(f'Here is your password: {words_generated_password})')

    else:
        length = st.slider('Password length (number of words):', 4, 8)
        capitalization = st.checkbox('Should words be capitalized?')
        seperator = st.text_input('Words are seperated with (for example ","):')
        all_capitalized= st.checkbox('Do you want all the words to be capitalized?')
        
        words_generated_password = words_password_generator(
            length,
            capitalization,
            all_capitalized,
            seperator,
            vocabulary=False
        )
        
        user_choice = st.toggle('Do you want to see your generated password?')
        if user_choice:
            st.success(f'Here is your password: {words_generated_password})')
            
elif password_type == 'Random':
    with st.form('my_form'):
        length = st.slider('Password Length:', 8, 16)
        include_letters = st.checkbox('Include letters?')
        include_numbers = st.checkbox('Include Numbers?')
        include_characters = st.checkbox('Include Characters (symbols)?')
        
        submitted = st.form_submit_button('Click to start generating password')
        if submitted:
            if any([include_letters, include_numbers, include_characters]):
                random_generated_password = random_password_generator(
                    length,
                    include_letters,
                    include_numbers,
                    include_characters
                )
    
                user_choice = st.toggle('Do you want to see your generated password?')
                if user_choice:
                        st.success(f'Here is your password: {random_generated_password})')
            else:
                st.info('Please select at least one option to generate a password.')
        
elif password_type == 'Memorable':
    length = st.slider('Password Length:', 8, 16)
    num = st.slider('Number of words in the password:', 1, 4)
    
    memorable_generated_password = memorable_password_generator(num)

    user_choice = st.toggle('Do you want to see your generated password?')
    if user_choice:
        st.success(f'Here is your password: {memorable_generated_password})')
