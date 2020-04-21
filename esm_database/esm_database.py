import sys
from . import getch

class DisplayDatabase():

    def __init__(self, tablename):
        if tablename == "experiments":
            from esm_runscripts import database
            self.entry_type = database.experiment
        else:
            print ("Unknown table, quitting...")
            sys.exit(-1)

        query = database.session.query(database.experiment)
        results = query.all()
        if not type(results) == list:
            results=[results]

        self.verbose = False
        self.all_results = results
        self.results = results
        table = getattr(self.entry_type, "__table__")
        columns = getattr(table, "columns")
        self.columns = [str(column).replace(tablename+".", "") for column in columns]

        while True:
            self.output_writer()
            self.decision_maker()


    def output_writer(self):
        print()
        if not self.verbose:
            getattr(self.entry_type, "topline")()
            #topline()
        for result in self.results:
            if self.verbose:
                getattr(self.entry_type, "nicer_output")(result)
            else:
                print (result)
        print ("------------------------------------------------------------------------------------------------------------------------------")
        print ("[S]elect Entry     [V]erbose on/off     [R]eset selection    [Edit] Entry                                               [Q]uit")
        print ("------------------------------------------------------------------------------------------------------------------------------")
   

    def ask_column(self:)
        find = input("Which column " + str(self.columns) + "? ").lower()

        if find == "":
            return None

        for column in self.columns:
            if column.startswith(find):
                find_column = column
                break

        if not find_column:
            print ("Unknown column.")
            return None

        return find_column


    def decision_maker(self):
        while True:
            char = getch.getch().lower()
            if char == "q":
                sys.exit(0)

            elif char == "v":
                self.verbose = not self.verbose
                break

            elif char == "s":
                find_column = self.ask_column()

                if not find_column:
                    break
            
                find_value = input("Search for? ")
                if find_value == "": 
                    break
            
                self.select_stuff(find_column, find_value)
                break

            elif char == "e":
                if len[self.results] == 0:
                    break
                elif len[self.results] == 1:
                    print ("Edit entry with id=" + self.results[0].id + " [y/n]?")
                    while True:
                        yesno = getch.getch().lower()
                        if yesno in ["y", "n"]:
                            break
                    if yesno == "y":
                        edit_id = self.results[0].id
                        edit_dataset = self.results[0]

                if not edit_id:
                    edit_id = int(input("Please enter id of the dataset you want to edit: "))
                    edit_dataset = [result in self.all_results if result.id == edit_id]
                    if edit_dataset == []:
                        print ("Unknown dataset id.")
                        break
                    else:
                        edit_dataset = edit_dataset[0]

                self.edit_dataset(edit_id, edit_dataset)
                break    

            elif char == "r":
                self.results = self.all_results
                break


    def edit_dataset(edit_id, edit_dataset):
        edit = input("Which column " + str(self.columns) + "? ").lower()

        if edit == "":
            return

        for column in self.columns:
            if column.startswith(edit):
                find_column = column 
                break

        if not find_column:
            print ("Unknown column.")
            return

        edit_entry = input("Change to? ")
        if edit_entry == "": 
            break
            



    def select_stuff(self, find_column, find_value):
        if find_column and find_value:
            if find_column == "id":
                self.results = [result for result in self.results if find_value == str(getattr(result, find_column))]
            else:
                self.results = [result for result in self.results if find_value in str(getattr(result, find_column))]



    #output_writer(database, verbose, results)
    #decision_maker(table, find, verbose, columns)
    #DisplayDatabase(table, find, verbose)
       
