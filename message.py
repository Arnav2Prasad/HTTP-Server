'''
request : 
    1st line : 
                1st word is method
                2nd word is URI
                3rd should be HTTP/1.1    (ends with \r\n)
    2nd line onwards:
            till we reach to \r\n\r\n
            Approach word till (":") OR (<spcace>) that is the header field
                skip ":" and trailing spaces --> all there till \r\n is header filed value
                
            AFTER \r\n\r\n : all the remaining conent is body
'''

'''
for response change the 1st line : that is -> HTTP/1.1 <status code> <status msg> /r/n
            rest remains same as there in request
'''


message=''
message += "GET /Content/themes/basic/vendors/fastclick/lib/fastclick.js HTTP/1.1"
message += "Host: portal.coep.org.in:9093"
message += "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0"
message += "Accept: */*"
message += "Accept-Language: en-US,en;q=0.5"
message += "Accept-Encoding: gzip, deflate"
message += "Connection: keep-alive"
message += "Referer: http://portal.coep.org.in:9093/"
message += "Cookie: _ga_TE06MZ3JNC=GS1.1.1717964486.13.0.1717964486.0.0.0; _ga=GA1.1.1329315096.1707154481; .ASPXAUTH=0D15AB82CCDBD503197BC7C48E097B77BCD90F741C664741DA8A1E989995819AF510267A4DDB1EA36E26D175EF2962E3127F8B3996D0095C2C4759744BBEC501747943D62668EA9445FFAC8DD298310732C7FDCC0C069CD0D50AE94C145D5BE0; ASP.NET_SessionId=0uc0dfz1ts2dckyahketgyux"


message=''
message += "HTTP/1.1 200 OK\r\n"
message += "Cache-Control: no-cache, no-store, must-revalidate\r\n"
message += "Pragma: no-cache\r\n"
message += "Content-Type: text/html; charset=utf-8\r\n"
message += "Expires: -1\r\n"
message += "Server: Microsoft-IIS/8.0\r\n"
message += "X-AspNetMvc-Version: 5.2\r\n"
message += "X-AspNet-Version: 4.0.30319\r\n"
message += "X-Powered-By: ASP.NET\r\n"
message += "Date: Wed, 12 Jun 2024 08:19:09 GMT\r\n"
message += "Content-Length: 850\r\n"
message += "\r\n"
message += "\r\n"
message += "<table border=\"0\" width=\"100%\" id="datatable\"  data-EditFunction=\"StudentAcademicEditUID\" data-DeleteFunction=\"StudentAcademicDelete\" class=\"table responsive-utilities table-bordered table-hover table-striped display dataTable\">"
message += ""
message += "<thead>"
message += "<tr>"
message += "<th>Sr.No.</th>"
message += "<th>"
message += "Name of Exam"
message += "</th>"
message += "<th>"
message += "NameOfSchool/Board/University"
message += "</th>"
message += "<th>"
message += "Year of Passing"
message += "</th>"
message += "<th>"
message += "Marks Obtained"
message += "</th>"
message += "<th>"
message += "Out of Marks"
message += "</th>"
message += "<th class=\"tableActions\">Actions</th>"
message += "</tr>"
message += "</thead>"
message += "<tbody>"
message += "</tbody>"
message += "</table>"
message += ""
