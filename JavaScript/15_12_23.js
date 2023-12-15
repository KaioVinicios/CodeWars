// 7 kyu 'Leap Years' by BattleRattle.
// Objective: return true or false if year is a leap year.

function isLeapYear(year) {
    if (year % 4 == 0 && (year % 400 == 0 || year % 100 != 0)) {
        return true
    }
    else {
        return false
    }
}