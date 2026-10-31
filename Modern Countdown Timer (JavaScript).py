/**
 * Calculates the time remaining until a target date.
 * @param {string} targetDate - Date string (e.g., "December 31, 2026 23:59:59")
 */
function getCountdown(targetDate) {
    const totalTime = Date.parse(targetDate) - Date.parse(new Date());

    if (totalTime <= 0) {
        return { expired: true };
    }

    const seconds = Math.floor((totalTime / 1000) % 60);
    const minutes = Math.floor((totalTime / 1000 / 60) % 60);
    const hours = Math.floor((totalTime / (1000 * 60 * 60)) % 24);
    const days = Math.floor(totalTime / (1000 * 60 * 60 * 24));

    return {
        expired: false,
        days,
        hours,
        minutes,
        seconds
    };
}

// Example usage:
const target = "December 31, 2026 23:59:59";
const timeLeft = getCountdown(target);

if (!timeLeft.expired) {
    console.log(`⏳ Countdown to New Year 2027:`);
    console.log(`${timeLeft.days} days, ${timeLeft.hours} hours, ${timeLeft.minutes} minutes, ${timeLeft.seconds} seconds remaining.`);
} else {
    console.log("The target date has already passed!");
}
