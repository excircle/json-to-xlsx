CREATE TABLE customer (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,  
    phone VARCHAR(100) NOT NULL,  
    package JSON, 
    PRIMARY KEY (id)
);

INSERT INTO customer (name, phone, package) VALUES (
    'John Doe',
    '123-456-7890',
    JSON_OBJECT(
        'package', 'family',
        'price', '$399.99',
        'redeemed', 'false',
        'package_members', JSON_OBJECT(
            'husband', 'john',
            'wife', 'jane',
            'kid', 'malort'
        )
    )
);
