(function() {

  function isStorageAlreadySaved(storage, key) {
    return storage.getItem(key) !== null;
  }

  function saveToStorage(storage, key) {
    storage.setItem(key, 'some value');
  }

  function setReportText(element, storage, key) {
    element.textContent =
      isStorageAlreadySaved(storage, key)
      ? 'not clear'
      : 'clear';
    console.log(element, 'text is', element.text);
  }

  const localKey = 'local-storage-test';
  const sessionKey = 'session-storage-test';


  window.onload = function() {
    const localStorageReport = document.getElementById(
      'local-storage-report');
    const sessionStorageReport = document.getElementById(
      'session-storage-report');
    setReportText(localStorageReport, localStorage, localKey);
    setReportText(sessionStorageReport, sessionStorage, sessionKey);
    console.log('saving to storage');
    saveToStorage(localStorage, localKey);
    saveToStorage(sessionStorage, sessionKey);
  };
})();
