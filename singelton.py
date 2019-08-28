class Singleton:
   __instance = None

   @staticmethod 
   def getInstance():
      """ Static  method. """
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance
   def __init__(self):
      if Singleton.__instance != None:
         raise Exception("Forbidden!")
      else:
         Singleton.__instance = self
