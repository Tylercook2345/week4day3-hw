-- List all customers who live in Texas (use JOINS)
select first_name, last_name, address_id
from customer
inner join address 
;



--Get all payments above $6.99 with the Customer's Full Name
select first_name, last_name
from customer 
where customer_id in (
	select customer_id
	from payment 
	group by customer_id
	having sum(amount) > 6.99
	order by sum(amount) desc

);

--Show all customers names who have made payments over $175 (use subqueries)
select first_name, last_name, store_id
from customer 
where customer_id in (
	select customer_id
	from payment 
	group by customer_id
	having sum(amount) > 175
	order by sum(amount) desc

);

--List all customers that live in Nepal (use the city table)
select city_id, city
from city 
where nepal;

--Which staff member had the most transactions?
select staff_id, payment_id
from payment;

--How many movies of each rating are there?
select count (distinct rating)
from film
 ;

--Show all customers who have made a single payment above $6.99 (use subqueries)
select amount 
from payment 
where amount = 6.99


-- how many free rentals did our stores give away?
select amount
from payment
where amount = 0;
