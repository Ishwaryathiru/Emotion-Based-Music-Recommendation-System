function opennav(){
    var sidePanel=document.getElementById("sidePanel")
    if(sidePanel.style.width=="0px")
    {
    sidePanel.style.width="25%";
}
else{
    sidePanel.style.width="0px";
}
}
document.addEventListener('DOMContentLoaded', function() {
    const monthDisplay = document.getElementById('monthDisplay');
    const calendarContainer = document.getElementById('calendarContainer');
    const nextBtn = document.getElementById('nextBtn');
  
    // Function to generate a calendar for a specific month and year
    function generateCalendar(year, monthIndex) {
      const currentDate = new Date(year, monthIndex);
      const firstDayOfMonth = new Date(year, monthIndex, 1);
      const lastDayOfMonth = new Date(year, monthIndex + 1, 0);
      const daysInMonth = lastDayOfMonth.getDate();
  
      monthDisplay.textContent = currentDate.toLocaleString('en-US', { month: 'long', year: 'numeric' });
  
      calendarContainer.innerHTML = '';
  
      // Create day headers
      const dayNames = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
      for (let i = 0; i < 7; i++) {
        const dayHeader = document.createElement('div');
        dayHeader.classList.add('day');
        dayHeader.textContent = dayNames[i];
        calendarContainer.appendChild(dayHeader);
      }
  
      // Fill in the dates
      let dayCounter = 1;
      for (let i = 0; i < 42; i++) {
        const dayCell = document.createElement('div');
        dayCell.classList.add('day');
        if (i >= firstDayOfMonth.getDay() && dayCounter <= daysInMonth) {
          dayCell.textContent = dayCounter;
          dayCounter++;
        }
        calendarContainer.appendChild(dayCell);
      }
    }
  
    // Initial calendar generation for the current month
    const currentDate = new Date();
    const currentYear = currentDate.getFullYear();
    const currentMonthIndex = currentDate.getMonth();
    generateCalendar(currentYear, currentMonthIndex);
  
    // Event listener for next month button
    nextBtn.addEventListener('click', function() {
      const nextMonthIndex = (currentMonthIndex + 1) % 12;
      const nextYear = nextMonthIndex === 0 ? currentYear + 1 : currentYear;
      generateCalendar(nextYear, nextMonthIndex);
    });
  });
