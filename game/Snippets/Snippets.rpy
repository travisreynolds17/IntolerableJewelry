# {
# 	// Place your snippets for python here. Each snippet is defined under a snippet name and has a prefix, body and 
# 	// description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
# 	// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the 
# 	// same ids are connected.
# 	// Example:
# 	// "Print to console": {
# 	// 	"prefix": "log",
# 	// 	"body": [
# 	// 		"console.log('$1');",
# 	// 		"$2"
# 	// 	],
# 	// 	"description": "Log output to console"
# 	// }

# 	"add chat message": {
# 		"prefix": "-addm",
# 		"body": [
# 			"\n\n\\$chat.addmessage(${1:speaker},\"${2:message}\")"
# 		],
# 		"description": "add chat message easily"
# 	},

# 	"bulk messages": {
# 		"prefix": "-bulkm",
# 		"body": [
# 			"\n\npython:\n\tnewComments = [\n\t\t[${1:speaker},\"${2:message}\"],\n\t\t[${3:speaker},\"${4:message}\"],\n\t\t[${5:speaker},\"${6:message}\"],\n\t\t[${7:speaker},\"${8:message}\"]\n\t]\n\n\t\\$chat.bulkMessage(newComments,${9:delay})"
# 		],
# 		"description": "Bulk messages"
# 	},

# 	"show story screen": {
# 		"prefix": "-story",
# 		"body": [
# 			"pause(0.5)\n\\$hideGui()\nscene bg ${1:screen} with fade\npause ${2:2.0}\npause\nscene bg ${3:screen}\npause(${4:0.5})\n\\$showGui()\npause ${5:0.5}"
# 		],
# 		"description": "Hide Gui, show a creepy text screen, show gui again"
# 	}
# }