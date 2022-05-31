ACCOUNT_CUR.execute(f'''
            UPDATE
                {ACCOUNT}
            SET
                points = 0
        ;''')

        ACCOUNT_CON.commit()

