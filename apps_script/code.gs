function onOpen() {
  const ui = SpreadsheetApp.getUi();
  ui.createMenu('🚀 School Agent')
      .addItem('1. Initialize Classes & Students', 'triggerSetup')
      .addSeparator()
      .addItem('2. Submit Grades to Server', 'submitGrades')
      .addToUi();
}

function triggerSetup() {
  const url = "https://api.shinobiautomation.com/start-setup";

  const options = {
    "method": "post",
    "contentType": "application/json"
  };

  try {
    UrlFetchApp.fetch(url, options);
    SpreadsheetApp.getUi().alert("⚙️ Setup Started! Please wait a moment for the tabs to appear.");
  } catch (e) {
    SpreadsheetApp.getUi().alert("❌ Connection Error. Is the server online?");
  }
}

function submitGrades() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = ss.getActiveSheet();
  const className = sheet.getName();

  const data = sheet.getDataRange().getValues();

  const gradesData = data.slice(1).map(row => {
    return {
      "id": row[0],
      "student_name": row[1],
      "grade": row[2]
    };
  });

  const payload = {
    "class_name": className,
    "students": gradesData
  };

  const options = {
    "method": "post",
    "contentType": "application/json",
    "payload": JSON.stringify(payload)
  };

  const url = "https://api.shinobiautomation.com/sync-grades";

  try {
    const response = UrlFetchApp.fetch(url, options);
    SpreadsheetApp.getUi().alert("✅ Grades submitted for " + className);
  } catch (e) {
    SpreadsheetApp.getUi().alert("❌ Error: Make sure your server is running!");
  }
}
