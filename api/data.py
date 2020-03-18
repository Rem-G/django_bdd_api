import pandas as pd
import os
from pathlib import Path
import sqlite3

class Data():

	def create_db(self, db_type, origine):
		"""
		db_type True : db_population
		db_type False : db_socialcategories
		"""
		path_excel = str(Path(os.getcwd()).parent) + origine
		com_dates = ["COM_1968", "COM_1975", "COM_1982", "COM_1990", "COM_1999", "COM_2006", "COM_2011", "COM_2016"]

		if db_type:
			filename = str(Path(os.getcwd()).parent) + "/bdd_api/db.sqlite3"
			skiprows = range(12)
			usecols = "E:AT"
		else:
			filename = str(Path(os.getcwd()).parent) + "/data/population_social_categories_1968-2016.db"
			skiprows = range(14)
			usecols = "E:R"

		conn = sqlite3.connect(filename)

		for sheet in com_dates:
			df = pd.read_excel(path_excel, sheet_name = sheet, skiprows = skiprows, usecols = usecols)
			df.columns = df.columns.str.replace(' ', '_')
			df.columns = df.columns.str.replace('\n', '_')
			df.columns = df.columns.str.replace('é', 'e')
			df.columns = df.columns.str.replace('è', 'e')
			df.columns = df.columns.str.replace('à', 'a')
			
			print(df.columns)

			df.to_sql('api_com_'+sheet.split('_')[1], conn, index = True, if_exists = "replace")
			print(sheet, "done")

		conn.commit()
		conn.close()

		print("Done")

#data = Data()
#data.create_db(True, "/bdd_api/pop-sexe-age-quinquennal6816.xls")

