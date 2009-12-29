set epoch to date "Thursday, January 1, 1970 00:00:00"

tell application "Skype"
	set textList to {}
	
	set calls to send command "SEARCH ACTIVECALLS" script name "My Script"
	set callId to last word of calls
	if callId is not "CALLS" then
		set AppleScript's text item delimiters to " "
		set partner to words 4 thru -1 of (send command "GET CALL " & callId & " PARTNER_DISPNAME" script name "My Script") as text
		set timestamp to words 4 thru -1 of (send command "GET CALL " & callId & " TIMESTAMP" script name "My Script") as text
		set AppleScript's text item delimiters to ""
		copy "Call: " & partner to the end of the textList
		copy timestamp to the end of the textList
	else
		set chats to send command "SEARCH RECENTCHATS" script name "My Script"
		set AppleScript's text item delimiters to " "
		set chats to text items of chats
		first item of chats
		set chats to rest of chats

		set AppleScript's text item delimiters to ","
		set chatIds to text items of chats
		set AppleScript's text item delimiters to ""

		set chatId to item 1 of chatIds
		if item -1 of chatId as text is "," then
			set chatId to (items 1 thru -2 of chatId as text)
		end if

		set AppleScript's text item delimiters to " "
		set topic to words 7 thru -1 of (send command "GET CHAT " & chatId & " FRIENDLYNAME " script name "My Script") as text
		set timestamp to epoch + (words 7 thru -1 of (send command "GET CHAT " & chatId & " TIMESTAMP" script name "My Script") as text)
		set AppleScript's text item delimiters to ""
		copy "Chat: " & topic to the end of the textList
		copy timestamp as text to the end of the textList
	end if
	set result to textList
end tell
