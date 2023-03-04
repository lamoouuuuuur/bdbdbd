CREATE TABLE IF NOT EXISTS client
(
    id serial not null primary key,
    surname varchar(40) not null,
    name varchar(40) not null,
    patronymic varchar(40) not null,
    number_phone varchar(40) not null
);

CREATE TABLE IF NOT EXISTS payment
(
    id serial not null primary key,
    client_id integer not null,
    foreign key (client_id) references client (id) on delete cascade
    on update cascade,
    date date not null,
    status status NOT NULL
);

CREATE TYPE status AS ENUM ('OK', 'NOT OK');

CREATE TABLE IF NOT EXISTS orders
(
    id serial not null primary key,
    client_id integer not null,
    foreign key (client_id) references client (id) on delete cascade
    on update cascade,
    order_value integer not null,
    order_status status NOT NULL,
    date_of_registration date not null,
    completion_date date
);

CREATE TABLE IF NOT EXISTS category
(
    id serial not null primary key,
    name varchar(40) not null
);

CREATE TABLE IF NOT EXISTS products
(
    id serial not null primary key,
    category_id integer not null,
    foreign key (category_id) references category (id) on delete
    cascade on update cascade,
    cost integer not null,
    name varchar(40) not null
);

CREATE TABLE IF NOT EXISTS ordering_product
(
    id serial not null primary key,
    order_id integer not null,
    foreign key (order_id) references orders (id) on delete cascade
    on update cascade,
    product_id integer not null,
    foreign key (product_id) references products (id) on delete
    cascade on update cascade,
    quantity integer not null
);

CREATE TABLE IF NOT EXISTS size
(
    id serial not null primary key,
    eng_name varchar(30) not null,
    rus_name varchar(30) not null
);

CREATE TABLE IF NOT EXISTS brand
(
    id serial not null primary key,
    name varchar(30) not null
);

CREATE TABLE IF NOT EXISTS color
(
    id serial not null primary key,
    name varchar(30) not null
);

CREATE TABLE IF NOT EXISTS wishlist
(
    id serial not null primary key,
    product_id integer not null,
    foreign key (product_id) references products (id) on delete
    cascade on update cascade,
    client_id integer not null,
    foreign key (client_id) references client (id) on delete cascade
    on update cascade
);

CREATE TABLE IF NOT EXISTS pickup_point
(
    id serial not null primary key,
    address varchar(255) not null,
    time_start date not null,
    time_end date not null,
    number_phone varchar not null
);

CREATE TABLE IF NOT EXISTS delivery
(
    id serial not null primary key,
    order_id integer not null,
    foreign key (order_id) references orders (id) on delete cascade
    on update cascade,
    pickup_point integer not null,
    foreign key (pickup_point) references pickup_point (id) on delete
    cascade on update cascade,
    delivery_cost decimal(10) not null,
    count_days integer not null
);

CREATE TABLE IF NOT EXISTS reviews
(
    id serial not null primary key,
    client_id integer not null,
    foreign key (client_id) references client (id) on delete cascade
    on update cascade,
    product_id integer not null,
    foreign key (product_id) references products (id) on delete
    cascade on update cascade,
    rate rating NOT NULL
);

CREATE TYPE rating AS ENUM ('1', '2', '3', '4', '5');