# A helper class & its functions to interact with Google Sheets using Python used in google colab

from google.colab import auth
import gspread
from google.auth import default
import pandas as pd

class GoogleSheets:
    """
    A class used to interact with googlesheets using python in Colab notebook

    Attributes
    ----------
    sheet_url : str
        a formatted string to print out what the animal says
    sheet_name : str
        the file of the GoogleSheet folder a user wants to use
    work_sheet : str
        a specific sheet in the Googlesheet file a user needs to access
    
    Methods
    -------
    returnClientObject(object_cred)
        returns credentials to interact with users googlesheets
   
    
    """

  def __init__(self,sheet_url,sheet_name,work_sheet):
    
    self.split_links = sheet_url.split('/')
    self.sheet_key = self.split_links[5]
    self.ss_name = sheet_name
    self.ws = work_sheet 

  def __str__(self):
    return "class instantiated for {} workbook and {} worksheet.".format(self.sheet_name,self.ws)

  def returnClientObject(self):
    auth.authenticate_user()
    creds, _ = default()
    return creds 

  def create_sheet(self,object_cred):
    self.object_cred = object_cred
    gc = gspread.authorize(self.object_cred)
    sh = gc.create(self.ss_name)

  def pull_sheet_todf(self,creds):
    self.creds = creds
    gc = gspread.authorize(self.creds)
    wb = gc.open_by_key(self.sheet_key)
    ws = wb.worksheet(self.ws)
    rows = ws.get_all_values()
    df = pd.DataFrame.from_records(rows[1:],columns=rows[0])
    return df

  def update_ghseets_fromdf(self,creds,data):
    self.worksheet = work_sheet
    self.creds = creds
    gc = gspread.authorize(self.creds)
    wb = gc.open_by_key(self.sheet_key)
    ws = wb.worksheet(self.ws)
    ws.update([data.columns.values.tolist()] + data.values.tolist() )
    return "{} has been updated with new data".format(self.ws)
  
  def clear_gsheets(self,creds):
    self.worksheet = work_sheet
    self.creds = creds
    gc = gspread.authorize(self.creds)
    wb = gc.open_by_key(self.sheet_key)
    ws = wb.worksheet(self.ws)
    ws.clear()
    return "{} has been wiped".format(self.ws)

