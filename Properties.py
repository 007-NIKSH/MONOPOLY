class Property:
    def __init__(self, Name, Colour, Owned, Cost, House):
        self.Name = Name
        self.Colour = Colour
        self.Owned = Owned
        self.Cost = Cost
        self.House = House
        self.Normal_Rent = int((Cost * 0.5) * 0.25)
        self.Colour_Set_Rent = int((Cost * 0.5) * 0.5)
        self.Settlement_1_Rent = int(Cost * 0.5)
        self.Settlement_2_Rent = int(Cost)
        self.Settlement_3_Rent = int(Cost + ((Cost * 30) / 100))
        self.Settlement_4_Rent = int(Cost + ((Cost * 60) / 100))
        self.City_Rent = int(Cost * 2)
        self.Bulid_Settlement_Cost = int((Cost * 50) / 100)
        self.Build_City_Cost = int((Cost * 70) / 100)

# Pr = ['Property1', 'Property2', 'Property3', 'Property4', 'Property5', 'Property6', 'Property7', 'Property8', 'Property9', 'Property10', 'Property11', 'Property12', 'Property13', 'Property14', 'Property15', 'Property16', 'Property17', 'Property18', 'Property19', 'Property20', 'Property21', 'Property22', 'Property23', 'Property24', 'Property25']
# Properties = ['Motor Drive', 'Gardget Wharf', 'Surfers Cove', 'Aqua Park', 'Lake Side Marina', 'Rail Way', 'Castle View', 'Dream Avenue', 'Palace Gardens', 'Adventure Park', 'Theme Park City', 'Movie District', 'Style Square', 'Air Way', 'Party Plaza', 'Show Time Boulevard', 'Sunshine Bay', 'Bling Beach', 'Water Way', 'Yatch Harbour', 'Tree Top Retreat', 'Ski Mountain', 'Diamond Hill', 'Fortune Valley', 'Paradise Island']
# Colour = ['Brown', 'Brown', 'Light Blue', 'Light Blue', 'Light Blue', 'White', 'Pink', 'Pink', 'Pink', 'Orange', 'Orange', 'Orange', 'Red', 'White', 'Red', 'Red', 'Yellow', 'Yellow', 'White', 'Yellow', 'Green', 'Green', 'Green', 'Dark Blue', 'dark Blue']
# Cost = [8, 11, 18, 23, 27, 36, 45, 50, 54, 63, 68, 72, 81, 36, 86, 90, 99, 104, 36, 108, 117, 122, 126, 144, 162]

# def Creat_Property(Properties, Colour, Cost, Pr):
#     x = 0
#     for x in range((len(Properties) - 1)):
#         pro = Properties[x]
#         colour = Colour[x]
#         cost = Cost[x]
#         P = Pr[x]

#         P = Property(pro, colour, False, cost, 0)
#         x += 1

# Pro1 = Property("MOTOR DRIVE", "BROWN", False, 8, 0)
# print(Pro1)
# print(Pro1.Name)
# print(Pro1.Colour)
# print(Pro1.Owned)
# print(Pro1.Cost)
# print(Pro1.House)
# print(Pro1.Normal_Rent)
# print(Pro1.Colour_Set_Rent)
# print(Pro1.Settlement_1_Rent)
# print(Pro1.Settlement_2_Rent)
# print(Pro1.Settlement_3_Rent)
# print(Pro1.Settlement_4_Rent)
# print(Pro1.City_Rent)
# print(Pro1.Bulid_Settlement_Cost)
# print(Pro1.Build_City_Cost)