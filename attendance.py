def attendance_percent(total_classes, attended_classes):
    return (attended_classes / total_classes) * 100

def attendance_suggestor(attendance_percentage):
    if attendance_percentage >= 75:
        return "You are doing well in attendance."
    elif attendance_percentage >= 50:
        return "You need to improve your attendance."
    else:
        return "Your attendance is very low. You need to take action."

def classes_suggestor(attendance_percentage, total_classes, attended_classes):
    remaining_classes = total_classes - attended_classes
    if attendance_percentage >= 75:
        return "You are doing well in attendance. You can miss up to {} more classes.".format(remaining_classes - (remaining_classes // 4))
    elif attendance_percentage >= 50:
        return "You need to improve your attendance. You should attend at least {} more classes.".format(total_classes // 2 - attended_classes)
    else:
        return "Your attendance is very low. You should attend all the remaining {} classes to improve your attendance.".format(remaining_classes)


total_classes = int(input("Enter the total number of classes: "))
attended_classes = int(input("Enter the number of classes attended: "))

percent = attendance_percent(total_classes, attended_classes)
print(f"Your attendance percentage is {percent}%.")

suggestion = attendance_suggestor(percent)
print(suggestion)

class_suggestion = classes_suggestor(percent, total_classes, attended_classes)
print(class_suggestion)
