// Makes the static deployment checklist interactive for each browser.
(function () {
  var STORAGE_KEY = "defender-deployment-checklist";

  function getChecklistItems() {
    return Array.prototype.slice.call(
      document.querySelectorAll(".task-list-item input[type='checkbox']")
    );
  }

  function loadSelections() {
    try {
      return JSON.parse(window.localStorage.getItem(STORAGE_KEY) || "{}");
    } catch (error) {
      return {};
    }
  }

  function saveSelections(items) {
    var selections = {};

    items.forEach(function (checkbox, index) {
      selections[index] = checkbox.checked;
    });

    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(selections));
  }

  function enableChecklist() {
    if (!window.location.pathname.includes("operations/deployment-checklist")) {
      return;
    }

    var items = getChecklistItems();
    var selections = loadSelections();

    items.forEach(function (checkbox, index) {
      checkbox.disabled = false;
      checkbox.checked = selections[index] === true;
      checkbox.addEventListener("change", function () {
        saveSelections(items);
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", enableChecklist);
  } else {
    enableChecklist();
  }
})();