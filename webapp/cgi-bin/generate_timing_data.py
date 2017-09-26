import cgi
import athletemodel
import cgitb
cgitb.enable()
import yate
athletelist = athletemodel.get_from_store()

form_data = cgi.FieldStorage()
athlete_name = form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header("Coach kelly's Timing Data"))
print(yate.header("Athlete"+athlete_name+",DOB:"+athletelist[athlete_name].dob+"."))
print(yate.para("The to times for this athlete are:"))
print(yate.u_list(athletelist[athlete_name].top3))
print(yate.include_footer({"Home":"/index.html","other athlete":"generate_list.py"}))
