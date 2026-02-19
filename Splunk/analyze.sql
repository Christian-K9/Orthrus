CREATE DATABASE all_logs;

CREATE TABLE alerts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message varchar(100),
    host varchar(20),
    user varchar(20),
    ip_address varchar(50),
    port int
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

GRANT SELECT, DELETE ON alerts.users TO 'alerts_user'@'localhost';