import csv

def normalize_birthplace(field):
    if field == "AK":
        return "Alaska"
    elif field == "ARK":
        return "Arkansas"
    elif field == "Aba" or field == "Alabama":
        return "Alabama"
    elif field == "Abbeville, S.C.":
        return "Abbeville, South Carolina"
    elif field == "Ala" or field == "Ala.":
        return "Alabama"
    elif field == "America" or field == "Amerika" or field == "American":
        return "America"
    elif field == "Apoplexy":
        return "Unknown"
    elif field == "Archer CO. Tex":
        return "Archer County, Texas"
    elif field == "Ark" or field == "Ark.":
        return "Arkansas"
    elif field == "Armenian":
        return "Armenia"
    elif field == "Astuin" or field == "Asutin" or field == "Ausitn" or field == "Ausrtin" or field == "Austin" or field == "Austin, TEx" or field == "Austin, TX" or field == "Austin, Tex" or field == "Austin, Tex." or field == "Austin, Tx" or field == "Austin, Tx." or field == "Austin. Tx" or field == "Austin1" or field == "AustinBlank" or field == "Austn" or field == "Autin" or field == "Austin TX" or field == "Austin Tex" or field == "Austin Texas" or field == "Austin, TEx":
        return "Austin, Texas"
    elif field == "Atlanic Ocean":
        return "Atlantic Ocean"
    elif field == "Baldwin Co., Tenn":
        return "Baldwin County, Tennessee"
    elif field == "Baltimore" or field == "Baltimore, MD":
        return "Baltimore, Maryland"
    elif field == "Bastrop" or field == "Bastrop, Tex" or field == "Bastrop Co" or field == "Bastrop Co." or field == "Bastrop Co. Tex" or field == "Bastrop County":
        return "Bastrop, Texas"
    elif field == "Beford Co. Tennessee":
        return "Bedford County, Tennessee"
    elif field == "Bell Co Tex" or field == "Bell Co, Texas" or field == "Bell County":
        return "Bell County, Texas"
    elif field == "Bexar Co":
        return "Bexar County, Texas"
    elif field == "Blanco Co." or field == "Blanco County" or field == "Blanco, TX":
        return "Blanco County, Texas"
    elif field == "Blank" or field == "Not Given" or field == "Not known":
        return "Unknown"
    elif field == "Bloomington, Ind.":
        return "Bloomington, Indiana"
    elif field == "Boerne, Tex":
        return "Boerne, Texas"
    elif field == "Bohemian":
        return "Bohemia"
    elif field == "Boston, Mass.":
        return "Boston, Massachusetts"
    elif field == "Brady, Tex":
        return "Brady, Texas"
    elif field == "Bremond, Tex":
        return "Bremond, Texas"
    elif field == "Brenham":
        return "Brenham, Texas"
    elif field == "Brights disease":
        return "Unknown"
    elif field == "Brown Co. Tex.":
        return "Brown County, Texas"
    elif field == "Brownsville" or field == "Brownsville, Tex.":
        return "Brownsville, Texas"
    elif field == "Brownwood, Tex.":
        return "Brownwood, Texas"
    elif field == "Bryan, Tex":
        return "Bryan, Texas"
    elif field == "Burnet" or field == "Burnet Co." or field == "Burnet County" or field == "Burnett Co." or field == "Burnett County" or field == "Burnette":
        return "Burnet County, Texas"
    elif field == "Cal" or field == "Cal.":
        return "California"
    elif field == "Caldwell Co." or field == "Caldwell Co., TX" or field == "Caldwell Co., Texas":
        return "Caldwell County, Texas"
    elif field == "Calvert, TX" or field == "Calvert, Tex":
        return "Calvert, Texas"
    elif field == "Canadian" or field == "Canady" or field == "Cannad" or field == "Cannady":
        return "Canada"
    elif field == "Carolina St.":
        return "Carolina Street"
    elif field == "Cedar Creek Tex":
        return "Cedar Creek, Texas"
    elif field == "Charleston, SC":
        return "Charleston, South Carolina"
    elif field == "Chautequa, New York":
        return "Chautauqua, New York"
    elif field == "Chicago" or field == "Chicago, IL" or field == "Chicago, Ill.":
        return "Chicago, Illinois"
    elif field == "Clarksville, City":
        return "Clarksville"
    elif field == "Claton, Miss":
        return "Clayton, Mississippi"
    elif field == "Cleburne, Tex.":
        return "Cleburne, Texas"
    elif field == "Cleveland [Ohio?]" or field == "Cleveland, Ohio":
        return "Cleveland, Ohio"
    elif field == "Co. Derry Ireland":
        return "County Derry, Ireland"
    elif field == "Col. Miss.":
        return "Columbus, Mississippi"
    elif field == "College Station Tex":
        return "College Station, Texas"
    elif field == "Comal Co.":
        return "Comal County, Texas"
    elif field == "Comfort, TX":
        return "Comfort, Texas"
    elif field == "Commerce (??)":
        return "Commerce"
    elif field == "Conecticut" or field == "Conn" or field == "Conn." or field == "Connecticutt":
        return "Connecticut"
    elif field == "Cotulla, TX":
        return "Cotulla, Texas"
    elif field == "County":
        return "Unknown"
    elif field == "Crockett Tex":
        return "Crockett, Texas"
    elif field == "Dallas" or field == "Dallas, TX" or field == "Dallas, Tex" or field == "Dallas, Tx" or field == "Dallas, Tx.":
        return "Dallas, Texas"
    elif field == "Decatur Co, Georgia":
        return "Decatur County, Georgia"
    elif field == "Decker Tr. Co.":
        return "Decker Travis County"
    elif field == "Dennison":
        return "Denison"
    elif field == "Denver, Col":
        return "Denver, Colorado"
    elif field == "Dublin, Ireland":
        return "Dublin, Ireland"
    elif field == "E. Texas":
        return "East Texas"
    elif field == "Eagle Lake, Tex":
        return "Eagle Lake, Texas"
    elif field == "Eagle Pass":
        return "Eagle Pass"
    elif field == "Edwards Co":
        return "Edwards County"
    elif field == "El Paso" or field == "El Paso, Tex":
        return "El Paso, Texas"
    elif field == "Elgin":
        return "Elgin, Texas"
    elif field == "Ellis Co., TX":
        return "Ellis County, Texas"
    elif field == "Erie, Pa.":
        return "Erie, Pennsylvania"
    elif field == "Europa":
        return "Europe"
    elif field == "Fannin County":
        return "Fannin County"
    elif field == "Fayette Co" or field == "Fayette Co.":
        return "Fayette County"
    elif field == "Fayette Co. Tex":
        return "Fayette County, Texas"
    elif field == "Fayettesville, N.C.":
        return "Fayette County, North Carolina"
    elif field == "Fiskville, Tex":
        return "Fiskville, Texas"
    elif field == "Fla" or field == "Flordia":
        return "Florida"
    elif field == "Ford Bend (Fort Bend)":
        return "Fort Bend County"
    elif field == "Fort Worth" or field == "Fort Worth, TX" or field == "Ft. Worth (?)":
        return "Fort Worth, Texas"
    elif field == "France Germany" or field == "Frensch (France)":
        return "France"
    elif field == "Frankfort, KY":
        return "Frankfort, Kentucky"
    elif field == "Franklin, Mo":
        return "Franklin, Missouri"
    elif field == "Fredeicksburg":
        return "Fredericksburg"
    elif field == "Frio Co":
        return "Frio County"
    elif field == "GA" or field == "Ga" or field == "Ga.":
        return "Georgia"
    elif field == "Gadnston":
        return "Gadsden"
    elif field == "Galveston" or field == "Galveston, TX":
        return "Galveston, Texas"
    elif field == "Geo." or field == "George":
        return "Georgia"
    elif field == "Georgetown" or field == "Georgetown, TX" or field == "Georgetown, Tex" or field == "Georgetown, Williamson Co.":
        return "Georgetown, Texas"
    elif field == "Georgis":
        return "Georgia"
    elif field == "Ger" or field == "Ger." or field == "Germ" or field == "Germ." or field == "German" or field == "Germank":
        return "Germany"
    elif field == "Gibralter":
        return "Gibraltar"
    elif field == "Gloster Co. Va.":
        return "Gloucester County, Virginia"
    elif field == "Goforth, Tex":
        return "Goforth, Texas"
    elif field == "Gonzales" or field == "Gonzales Co." or field == "Gonzales, Tex" or field == "Gonzales, Texas":
        return "Gonzales, Texas"
    elif field == "Govalle, Tex.":
        return "Govalle, Texas"
    elif field == "Grece":
        return "Greece"
    elif field == "Halifax, VA":
        return "Halifax, Virginia"
    elif field == "Harris Co Tex" or field == "Harris Co, TX" or field == "Harris Co." or field == "Harris Co. TX" or field == "Harris County, Texas" or field == "Harrison Co.":
        return "Harrison County, Texas"
    elif field == "Hays Co" or field == "Hays Co." or field == "Hays Co., Texas" or field == "Hays County" or field == "Hays County, TX":
        return "Hays County, Texas"
    elif field == "Hempstead" or field == "Hempstead, TX" or field == "Hemstead, Tx":
        return "Hempstead, Texas"
    elif field == "Henryitta, Okla":
        return "Henrietta, Oklahoma"
    elif field == "Hessen Germany":
        return "Hessen, Germany"
    elif field == "Hill Co":
        return "Hill County"
    elif field == "Hokley":
        return "Hockley"
    elif field == "Houston" or field == "Houston Tex" or field == "Houston, TX" or field == "Houston, Tex" or field == "Houston, Tx" or field == "Houston, Tx.":
        return "Houston, Texas"
    elif field == "Hungaria":
        return "Hungary"
    elif field == "Huntsville, Tex.":
        return "Huntsville, Texas"
    elif field == "ILL" or field == "Ill" or field == "Ill USA" or field == "Ill." or field == "Illegible" or field == "Illinios" or field == "Illinois  (????)" or field == "Illninois" or field == "Illnois" or field == "Ills":
        return "Illinois"
    elif field == "Ind" or field == "Ind." or field == "Inda (??)" or field == "Indanan [?]" or field == "Indian Nation" or field == "Indian Territory":
        return "Indiana"
    elif field == "Irleand" or field == "Irlend":
        return "Ireland"
    elif field == "Italia" or field == "Italia (Italy)" or field == "Italy (?)":
        return "Italy"
    elif field == "Jasper Co. Tex":
        return "Jasper County, Texas"
    elif field == "Jefferson City, Mo.":
        return "Jefferson City, Missouri"
    elif field == "Jew":
        return "Unknown"
    elif field == "Joplin Mo":
        return "Joplin, Missouri"
    elif field == "KY" or field == "Kentuky" or field == "Ky" or field == "Ky.":
        return "Kentucky"
    elif field == "Kansas City, M":
        return "Kansas City, Missouri"
    elif field == "Kaufman Co":
        return "Kaufman County"
    elif field == "Ken (tucky)?" or field == "Ken." or field == "Kentucky, U.S." or field == "Kentuky":
        return "Kentucky"
    elif field == "LA" or field == "La" or field == "La (?)":
        return "Louisiana"
    elif field == "LaGrange" or field == "LaGrange, Fayete Co." or field == "Lagrange, Texas":
        return "La Grange, Texas"
    elif field == "Lareda, Tex" or field == "Laredo" or field == "Laredo, Tex" or field == "Laredo, Tex.":
        return "Laredo, Texas"
    elif field == "Lavaca Co.":
        return "Lavaca County"
    elif field == "Lee Co. Tex":
        return "Lee County, Texas"
    elif field == "Leesburg, La.":
        return "Leesburg, Louisiana"
    elif field == "Leon Co., Tex.":
        return "Leon County, Texas"
    elif field == "Lexington Ky":
        return "Lexington, Kentucky"
    elif field == "Liberty Co. Tex":
        return "Liberty County, Texas"
    elif field == "Limestone Co., TX":
        return "Limestone County, Texas"
    elif field == "Linchburg, Virginia":
        return "Lynchburg, Virginia"
    elif field == "Lincoln Co, North Carolina":
        return "Lincoln County, North Carolina"
    elif field == "Llano":
        return "Llano, Texas"
    elif field == "Llano Co., Texas":
        return "Llano County, Texas"
    elif field == "Lockhart" or field == "Lockhart, Tex":
        return "Lockhart, Texas"
    elif field == "Louisanna" or field == "Lousiana":
        return "Louisiana"
    elif field == "Louisville, Ky.":
        return "Louisville, Kentucky"
    elif field == "Luling, Tex":
        return "Luling, Texas"
    elif field == "MA (?)" or field == "Mass" or field == "Mass (Miss)" or field == "Mass." or field == "Massachusetts (????)":
        return "Massachusetts"
    elif field == "Main":
        return "Maine"
    elif field == "Madison Co.":
        return "Madison County"
    elif field == "Manor" or field == "Manor, TX" or field == "Manor, Tex":
        return "Manor, Texas"
    elif field == "Marshall, Tex.":
        return "Marshall, Texas"
    elif field == "Mason Co.":
        return "Mason County"
    elif field == "Md" or field == "Md.":
        return "Maryland"
    elif field == "Memphis, Ten" or field == "Memphis, Tenn":
        return "Memphis, Tennessee"
    elif field == "Mex" or field == "Mex." or field == "Mexican":
        return "Mexico"
    elif field == "Mich" or field == "Mich.":
        return "Michigan"
    elif field == "Milam Co. TX":
        return "Milam County, Texas"
    elif field == "Millerville, Ga":
        return "Millerville, Georgia"
    elif field == "Millitair Institute":
        return "Military Institute"
    elif field == "Minn" or field == "Minn.":
        return "Minnesota"
    elif field == "Misisipi (Mississippi)" or field == "Miss" or field == "Miss (??)" or field == "Miss." or field == "Missippi" or field == "Missisipi" or field == "Missisippi":
        return "Mississippi"
    elif field == "Misouri (Missouri)" or field == "Missouri" or field == "Missouri (Misouria)" or field == "Missouri (Missouria)" or field == "Missoury" or field == "Missoury(Missouri)" or field == "Mo" or field == "Mo.":
        return "Missouri"
    elif field == "Mobile" or field == "Mobile Ala" or field == "Mobile, Ala" or field == "Mobile, Alabama" or field == "Mobile, Louisiana":
        return "Mobile, Alabama"
    elif field == "Morris Co.":
        return "Morris County"
    elif field == "N C" or field == "N Carolina" or field == "N. Carolina" or field == "N. Carolina":
        return "North Carolina"
    elif field == "N H" or field == "N.H.":
        return "New Hampshire"
    elif field == "N York" or field == "N.Y." or field == "NY" or field == "NY (?)" or field == "NY City" or field == "NY State" or field == "New Yrok":
        return "New York"
    elif field == "N. Jersey" or field == "New jersey":
        return "New Jersey"
    elif field == "Nachodothis, Texas" or field == "Nacogdoches, Tex":
        return "Nacogdoches, Texas"
    elif field == "Nashville Tenn" or field == "Nashville, Tenn":
        return "Nashville, Tennessee"
    elif field == "Natchez, Miss":
        return "Natchez, Mississippi"
    elif field == "Native Texas" or field == "Native Texian":
        return "Texas"
    elif field == "Navasota" or field == "Navasota Co.":
        return "Navasota County, Texas"
    elif field == "Neorgia":
        return "Georgia"
    elif field == "New Braunfels":
        return "New Braunfels, Texas"
    elif field == "New Orleans" or field == "New Orleans La" or field == "New Orleans, LA" or field == "New Orleans, La":
        return "New Orleans, Louisiana"
    elif field == "No Record" or field == "Not Given" or field == "Not Known" or field == "not given" or field == "not known":
        return "Unknown"
    elif field == "Okla":
        return "Oklahoma"
    elif field == "Onion Creek" or field == "Onion Creek, T.Co.":
        return "Onion Creek, Travis County"
    elif field == "Pa" or field == "Pa." or field == "Penn" or field == "Penn.":
        return "Pennsylvania"
    elif field == "Philadelphia" or field == "Philiadelphia" or field == "Philiadelphia, Pennsylvania" or field == "Philpa (?)":
        return "Philadelphia, Pennsylvania"
    elif field == "Pittsburg":
        return "Pittsburgh, Pennsylvania"
    elif field == "Polk Co. Texas":
        return "Polk County, Texas"
    elif field == "Porto Rico":
        return "Puerto Rico"
    elif field == "Portsmouth, Eng":
        return "Portsmouth, England"
    elif field == "Prussian":
        return "Prussia"
    elif field == "Quincy, Ill.":
        return "Quincy, Illinois"
    elif field == "R.I.":
        return "Rhode Island"
    elif field == "Raleigh, N C":
        return "Raleigh, North Carolina"
    elif field == "Republic of Texas":
        return "Texas"
    elif field == "Rich, VA" or field == "Richmond, Va.":
        return "Richmond, Virginia"
    elif field == "Roanoak":
        return "Roanoke"
    elif field == "Robertson Co. TX" or field == "Robertson Co., Tx" or field == "Robinson Co. (Robertson)":
        return "Robertson County, Texas"
    elif field == "Rockport, Tex":
        return "Rockport, Texas"
    elif field == "Round Rock" or field == "Round Rock Texas":
        return "Round Rock, Texas"
    elif field == "Rusk Co., Tex" or field == "Rusk County, Tex":
        return "Rusk County, Texas"
    elif field == "Rutledge, TX":
        return "Rutledge, Texas"
    elif field == "S C" or field == "S Carolina" or field == "S. C." or field == "S. Carolina" or field == "S.C." or field == "SC" or field == "So Carolina" or field == "South C." or field == "South Car." or field == "South Caroline":
        return "South Carolina"
    elif field == "Sallito, Miss.":
        return "Sallito, Mississippi"
    elif field == "San Antonio" or field == "San Antonio Tex" or field == "San Antonio, Tex" or field == "San Antonio, Texas" or field == "San Atonio":
        return "San Antonio, Texas"
    elif field == "San Luis Potosi" or field == "San Luis Potosi, Mex.":
        return "San Luis Potosi, Mexico"
    elif field == "San Marcos" or field == "San Marcos (?)" or field == "San Marcos [TX]" or field == "San Marcos, Hays Co.":
        return "San Marcos, Texas"
    elif field == "Sanders, TN":
        return "Sanders, Tennessee"
    elif field == "Saxony" or field == "Saxony, Germany":
        return "Saxony, Germany"
    elif field == "Schleswig Holstein":
        return "Schleswig-Holstein"
    elif field == "Scottland":
        return "Scotland"
    elif field == "Scottville, TX":
        return "Scottville, Texas"
    elif field == "Selma, Ala":
        return "Selma, Alabama"
    elif field == "Shannon, Miss":
        return "Shannon, Mississippi"
    elif field == "Shreport La":
        return "Shreveport, Louisiana"
    elif field == "So Carolina" or field == "So. Caroline" or field == "South Caroline":
        return "South Carolina"
    elif field == "St Louis" or field == "St Louis Mo" or field == "St Louis, Mo":
        return "St. Louis, Missouri"
    elif field == "St. Antonio" or field == "St. Antonion":
        return "San Antonio"
    elif field == "St. Louis, Mo.":
        return "St. Louis, Missouri"
    elif field == "St. Marcos, Hays Co.":
        return "San Marcos, Texas"
    elif field == "State Lun. Asy.":
        return "Austin State Hospital"
    elif field == "Stephenburg":
        return "Stephensburg"
    elif field == "Suffocation":
        return "Unknown"
    elif field == "Sweden (?)" or field == "Swedish":
        return "Sweden"
    elif field == "Sweland" or field == "Swisher(Swiss)" or field == "Swiss" or field == "Swissland (?)":
        return "Switzerland"
    elif field == "TX" or field == "tEXAS" or field == "tEXAS" or field == "Tex" or field == "Tex." or field == "Texa" or field == "Texasd" or field == "Texs" or field == "Texsa" or field == "Texxas":
        return "Texas"
    elif field == "Taylor" or field == "Taylor [TX]" or field == "Taylor, Tex" or field == "Taylor, Tex.":
        return "Taylor, Texas"
    elif field == "Templeton, Mass.":
        return "Templeton, Massachusetts"
    elif field == "Ten" or field == "Ten." or field == "Tenn" or field == "Tenn (?)" or field == "Tenn.":
        return "Tennessee"
    elif field == "Tex" or field == "Tex." or field == "Texas":
        return "Texas"
    elif field == "Travis" or field == "Travis CO." or field == "Travis Co" or field == "Travis Co Tex" or field == "Travis Co, Tex" or field == "Travis Co, Texas" or field == "Travis Co." or field == "Travis Co. TX" or field == "Travis Co. Tex" or field == "Travis Co. Tex.":
        return "Travis County, Texas"
    elif field == "Travis County":
        return "Travis County, Texas"
    elif field == "U. S." or field == "U.S." or field == "U.S.A." or field == "USA":
        return "United States"
    elif field == "Upsom Co, GA":
        return "Upson County, Georgia"
    elif field == "VA" or field == "Va" or field == "Va.":
        return "Virginia"
    elif field == "Valverde(?) Tex":
        return "Val Verde County, Texas"
    elif field == "Victoria Co.":
        return "Victoria County, Texas"
    elif field == "Virginia (?)":
        return "Virginia"
    elif field == "W. Va." or field == "W. Virginia" or field == "West VA" or field == "West Va":
        return "West Virginia"
    elif field == "Waco" or field == "Waco Texas" or field == "Waco, Tex":
        return "Waco, Texas"
    elif field == "Waller Co, Texas" or field == "Waller Co. Tex." or field == "Waller Co." or field == "Waller County":
        return "Waller County, Texas"
    elif field == "Wash Co. Tex" or field == "Wash Co. Texas":
        return "Washington County, Texas"
    elif field == "Washington Co" or field == "Washington Co.":
        return "Washington County"
    elif field == "Washington D C" or field == "Washington DC" or field == "Washington, D C" or field == "Washington, D.C.":
        return "Washington, D.C."
    elif field == "Washington, TX":
        return "Washington, Texas"
    elif field == "Webberville" or field == "Webberville Tex" or field == "Webberville, TX":
        return "Webberville, Texas"
    elif field == "Whales (Wales)":
        return "Wales"
    elif field == "Wheatville":
        return "Wheatsville"
    elif field == "Wheelock, Tex.":
        return "Wheelock, Texas"
    elif field == "Williams Co. (Williamson?)" or field == "Williams Co.(Williamson)" or field == "Williamson Co" or field == "Williamson Co." or field == "Williamson Co. Texas" or field == "Williamson County":
        return "Williamson County, Texas"
    elif field == "Williamton N C":
        return "Williamton, North Carolina"
    elif field == "Willis":
        return "Willis"
    elif field == "Wilson Co.":
        return "Wilson County, Texas"
    elif field == "Wis" or field == "Wis.":
        return "Wisconsin"
    elif field == "Wisconsin":
        return "Wisconsin"
    elif field == "Yorktown, Tx":
        return "Yorktown, Texas"
    elif field == "Zavalla Co":
        return "Zavala County, Texas"

   # Add more conditions here as needed
    
    # If no match found, return the original field
    return field

with open('combined.csv', 'r') as infile, open('normalized_birthplace.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    header = next(reader)  # Read and store the header row
    writer.writerow(['pkoakwood', 'nativity'])  # Write the modified header to the output file

    for row in reader:
        original_field = row[7]  # Assuming birthplace is in the 8th column
        normalized_field = normalize_birthplace(original_field)
        
        if normalized_field != original_field:  # Only write the row if the data has changed
            writer.writerow([row[0], normalized_field])  # Write the modified columns to the output file
