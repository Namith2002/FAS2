/**
 * Reports JavaScript functionality
 * Handles report generation and visualization
 */

document.addEventListener('DOMContentLoaded', function() {
    // Check if we're on the reports page
    if (window.location.href.includes('reports')) {
        initReportsPage();
    }
});

function initReportsPage() {
    console.log('Initializing Reports page');
    
    // Initialize report card buttons
    initReportCardButtons();
    
    // Initialize custom report form
    initCustomReportForm();
    
    // Initialize charts
    initReportCharts();
}

function initReportCardButtons() {
    const viewButtons = document.querySelectorAll('.report-card .btn:first-child');
    const downloadButtons = document.querySelectorAll('.report-card .btn:last-child');
    
    viewButtons.forEach(button => {
        button.addEventListener('click', function() {
            const reportTitle = this.closest('.report-card').querySelector('.card-title').textContent;
            console.log(`Viewing report: ${reportTitle}`);
            
            // This would typically show a modal or navigate to a detailed view
            alert(`Viewing ${reportTitle}`);
        });
    });
    
    downloadButtons.forEach(button => {
        button.addEventListener('click', function() {
            const reportTitle = this.closest('.report-card').querySelector('.card-title').textContent;
            console.log(`Downloading report: ${reportTitle}`);
            
            // This would typically trigger a download
            alert(`Downloading ${reportTitle} as PDF`);
        });
    });
}

function initCustomReportForm() {
    const customReportForm = document.getElementById('custom-report-form');
    
    if (customReportForm) {
        customReportForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form data
            const formData = new FormData(this);
            const reportData = {};
            
            for (const [key, value] of formData.entries()) {
                reportData[key] = value;
            }
            
            console.log('Generating custom report with data:', reportData);
            
            // This would typically make an AJAX call to generate the report
            alert('Generating custom report...');
        });
        
        // Handle date range selection
        const dateRange = document.getElementById('date-range');
        const customDateRange = document.getElementById('custom-date-range');
        
        if (dateRange && customDateRange) {
            dateRange.addEventListener('change', function() {
                if (this.value === 'custom') {
                    customDateRange.style.display = 'flex';
                } else {
                    customDateRange.style.display = 'none';
                }
            });
        }
    }
}

function initReportCharts() {
    console.log('Initializing report charts');
    
    // This would initialize charts using a library like Chart.js
    // Example:
    // const ctx = document.getElementById('attendance-chart').getContext('2d');
    // new Chart(ctx, { type: 'bar', data: {...}, options: {...} });
}