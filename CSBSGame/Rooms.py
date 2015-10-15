

class Rooms(object):
    def __init__(self):
        self.data = []
        self.popRooms()

    def popRooms(self):
        rooms = ['George Allen Field', 'Japanese Garden', 'Student Parking', 'The Pyramid', 'West Walkway',
                 'Rec Center', 'Forbidden Parking', 'Library', 'LA 5' , 'Bratwurst Hall', 'East Walkway',
        'Computer Lab', 'North Hall', 'Room of Retirement', 'ECS 302', 'South Hall', 'Elevators', 'ECS 308',
                 'EAT Club', 'CECS Conference Room', 'Lactation Lounge']
        return rooms

    def roomConnections(self, value):
        dict = {
             'South Hall': ['South Hall','ECS 302','EAT Club', 'CECS Conference Room', 'Lactation Lounge','ECS 308','East Walkway',
                           'North Hall','Computer Lab','Room of Retirement','Elevators', 'LA 5', 'Library','Rec Center',
		'George Allen Field','Forbidden Parking','Bratwurst Hall','Student Parking','North Hall','Computer Lab','Room of Retirement',],

'ECS 308': ['ECS 308','South Hall','ECS 302','EAT Club', 'CECS Conference Room', 'Lactation Lounge','East Walkway',
		'Forbidden Parking','Bratwurst Hall', 'North Hall','West Walkway', 'Computer Lab', 'Room of Retirement'],

'Lactation Lounge': ['Lactation Lounge','South Hall','ECS 308','ECS 302','EAT Club', 'CECS Conference Room','East Walkway',
		'Forbidden Parking','Bratwurst Hall', 'North Hall','West Walkway','Computer Lab', 'Room of Retirement'],

'George Allen Field':['George Allen Field','Japanese Garden','Pyramid','Rec Center','West Walkway', 'Student Parking',
		 'East Walkway', 'Library', 'LA 5','North Hall', 'Computer Lab','ECS 302','Elevators','Room of Retirement','South Hall'],

'Japanese Garden':['Japanese Garden','George Allen Field','Pyramid','Student Parking','Forbidden Parking', 'East Walkway',
		'Rec Center', 'West Walkway', 'North Hall', 'Library'],

'Pyramid':['Pyramid','George Allen Field','West Walkway', 'Library','North Hall',
		'Forbidden Parking', 'East Walkway','Japanese Garden','Rec Center','Student Parking'],

'Rec Center':['Rec Center','George Allen Field', 'Japanese Garden', 'Student Parking', 'The Pyramid', 'West Walkway',
                 'Forbidden Parking', 'Library', 'LA 5' , 'Bratwurst Hall', 'East Walkway','Computer Lab', 'North Hall',
		'Room of Retirement', 'ECS 302', 'South Hall', 'Elevators', 'ECS 308','EAT Club', 'CECS Conference Room', 'Lactation Lounge'],

'Student Parking':['Student Parking','George Allen Field', 'Japanese Garden', 'The Pyramid', 'West Walkway',
                 'Rec Center', 'Forbidden Parking', 'Library', 'Bratwurst Hall', 'East Walkway','North Hall', 'South Hall'],

'Forbidden Parking':['Forbidden Parking','George Allen Field', 'Japanese Garden', 'Student Parking', 'The Pyramid', 'West Walkway',
                 'Rec Center', 'Library', 'LA 5' , 'Bratwurst Hall', 'East Walkway', 'North Hall', 'ECS 302', 'South Hall', 'ECS 308',
                 'EAT Club', 'CECS Conference Room', 'Lactation Lounge'],

'East Walkway':['East Walkway','George Allen Field', 'Japanese Garden', 'Student Parking', 'The Pyramid', 'West Walkway',
                 'Rec Center', 'Forbidden Parking', 'Library', 'LA 5' , 'Bratwurst Hall', 'Computer Lab', 'North Hall',
		'Room of Retirement', 'ECS 302', 'South Hall', 'Elevators', 'ECS 308',
                 'EAT Club', 'CECS Conference Room', 'Lactation Lounge'],

'Bratwurst Hall':['Bratwurst Hall','East Walkway','LA 5','North Hall', 'Elevators', 'West Walkway','South Hall', 'ECS 308', 'Lactation Lounge',
			'CECS Conference Room', 'EAT Club', 'ECS 302', 'Forbidden Parking', 'Rec Center','Student Parking'],

'LA 5':['LA 5','Bratwurst Hall','Library','Elevators','North Hall', 'South Hall', 'Computer Lab', 'ECS 302', 'Room of Retirement', 'West Walkway', 'East Walkway',
		'Rec Center', 'George Allen Field'],

'Library':['Library','LA 5','West Walkway', 'North Hall', 'South Hall', 'Computer Lab', 'Elevators',
		'ECS 302', 'Room of Retirement','Bratwurst Hall', 'East Walkway','George Allen Field', 'Pyramid', 'Rec Center','Japanese Garden',
		'Student Parking', 'Forbidden Parking' ],

'West Walkway':['West Walkway','George Allen Field', 'Japanese Garden', 'Student Parking', 'The Pyramid',
                 'Rec Center', 'Forbidden Parking', 'Library', 'LA 5' , 'Bratwurst Hall', 'East Walkway',
        	'Computer Lab', 'North Hall', 'Room of Retirement', 'ECS 302', 'South Hall', 'Elevators', 'ECS 308',
                 'EAT Club', 'CECS Conference Room', 'Lactation Lounge'],

'Computer Lab':['Computer Lab','North Hall','Room of Retirement','North Hall','EAT Club','ECS 308','South Hall','ECS 302',
		 'CECS Conference Room', 'Lactation Lounge','East Walkway','Elevators', 'LA 5','West Walkway',
		 'Library','Rec Center', 'George Allen Field'],

'ECS 302':['ECS 302','North Hall','South Hall','ECS 308','EAT Club', 'CECS Conference Room', 'Lactation Lounge','East Walkway','Elevators',
		'Forbidden Parking','Bratwurst Hall','West Walkway', 'LA 5','Computer Lab', 'Room of Retirement', 'Library', 'Rec Center', 'George Allen Field'],

'EAT Club':['EAT Club','ECS 308','South Hall','ECS 302', 'CECS Conference Room', 'Lactation Lounge','East Walkway','Elevators',
		'Forbidden Parking','Bratwurst Hall', 'North Hall','West Walkway','Computer Lab', 'Room of Retirement'],

 'CECS Conference Room':['CECS Conference Room','South Hall','ECS 308','Elevators','ECS 302','EAT Club','Lactation Lounge','East Walkway',
		'Forbidden Parking','Bratwurst Hall', 'North Hall','West Walkway','Computer Lab', 'Room of Retirement'],

'Elevators':['Elevators','North Hall','South Hall','LA 5','Computer Lab', 'Room of Retirement', 'ECS 302', 'ECS 308',
		 'EAT Club', 'CECS Conference Room', 'Lactation Lounge','East Walkway','Library', 'Bratwurst Hall', 'West Walkway', 'George Allen Field',
			'Rec Center'],

'North Hall':['North Hall','West Walkway','Computer Lab','Room of Retirement','ECS 302','Elevators','South Hall','East Walkway','EAT Club','ECS 308',
		'CECS Conference Room', 'Lactation Lounge','George Allen Field', 'Pyramid', 'Japanese Garden',
		'Rec Center','Bratwurst Hall', 'Forbidden Parking','Student Parking','Library', 'LA 5'],

'Room of Retirement':['Room of Retirement','North Hall','EAT Club','ECS 308','South Hall','ECS 302',
		 'CECS Conference Room', 'Lactation Lounge','East Walkway','Computer Lab','Elevators', 'LA 5','West Walkway',
		 'Library','Rec Center', 'George Allen Field']
	    }
        return dict[value]

    def roomCoords(self, key):
        dict = {
            'South Hall':  [850,1170],
            'ECS 308':	[850,1350],
            'Lactation Lounge': [1230,1350],
            'George Allen Field':  [60,50],
            'Japanese Garden':	[460,50],
            'Pyramid':	[445,290],
            'Rec Center':	[460,570],
            'Student Parking':	[960,50],
            'Forbidden Parking':	[1060,520],
            'East Walkway':	[1480,1110],
            'Bratwurst Hall':	[1100,1670],
            'LA 5':		[490,1670],
            'Library':		[60,1670],
            'West Walkway':	[60,660],
            'Computer Lab':	[200,900],
            'ECS 302':		[630,900],
            'EAT Club':		[1060,900],
            'CECS Conference Room':[1270,900],
            'Elevators':	[630,1350],
            'North Hall':	[210,1170],
            'Room of Retirement': [200,1350]
        }
        return dict[key]