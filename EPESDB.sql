--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.12
-- Dumped by pg_dump version 9.5.12

-- Started on 2018-04-21 14:38:13 PDT

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 2204 (class 1262 OID 16393)
-- Name: EPES; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE "EPES" WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';


ALTER DATABASE "EPES" OWNER TO postgres;

\connect "EPES"

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 1 (class 3079 OID 12393)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2207 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 181 (class 1259 OID 16394)
-- Name: department; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.department (
    department_id character varying(16) NOT NULL,
    name character varying(32) NOT NULL,
    head character varying(16)
);


ALTER TABLE public.department OWNER TO postgres;

--
-- TOC entry 183 (class 1259 OID 16404)
-- Name: employee; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.employee (
    employee_id character varying(16) NOT NULL,
    name character varying(32) NOT NULL,
    department character varying(16) NOT NULL,
    role character varying(16) NOT NULL
);


ALTER TABLE public.employee OWNER TO postgres;

--
-- TOC entry 184 (class 1259 OID 16419)
-- Name: login_information; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.login_information (
    username character varying(16) NOT NULL,
    password character varying(16) NOT NULL,
    employee_id character varying(16) NOT NULL
);


ALTER TABLE public.login_information OWNER TO postgres;

--
-- TOC entry 188 (class 1259 OID 16470)
-- Name: rating_comment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.rating_comment (
    rating_comment_id character varying(16) NOT NULL,
    comment text,
    rating_report_id character varying(16)
);


ALTER TABLE public.rating_comment OWNER TO postgres;

--
-- TOC entry 189 (class 1259 OID 16483)
-- Name: rating_reply; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.rating_reply (
    rating_reply_id character varying(16) NOT NULL,
    comment text,
    rating_comment_id character varying(16)
);


ALTER TABLE public.rating_reply OWNER TO postgres;

--
-- TOC entry 187 (class 1259 OID 16444)
-- Name: rating_report; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.rating_report (
    rating_report_id character varying(16) NOT NULL,
    report text,
    reportee character varying(16),
    reporter character varying(16)
);


ALTER TABLE public.rating_report OWNER TO postgres;

--
-- TOC entry 182 (class 1259 OID 16399)
-- Name: role; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.role (
    role_id character varying(16) NOT NULL,
    title character varying(32) NOT NULL,
    "isManager" boolean NOT NULL
);


ALTER TABLE public.role OWNER TO postgres;

--
-- TOC entry 185 (class 1259 OID 16429)
-- Name: salary; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.salary (
    salary_id character varying(16) NOT NULL,
    wage double precision NOT NULL,
    bonus double precision
);


ALTER TABLE public.salary OWNER TO postgres;

--
-- TOC entry 186 (class 1259 OID 16434)
-- Name: work_day; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.work_day (
    day date NOT NULL,
    employee_id character varying(16) NOT NULL,
    salary character varying(16) NOT NULL,
    hours double precision NOT NULL
);


ALTER TABLE public.work_day OWNER TO postgres;

--
-- TOC entry 2190 (class 0 OID 16394)
-- Dependencies: 181
-- Data for Name: department; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.department (department_id, name, head) VALUES ('BE1', 'Back End', 'sf');
INSERT INTO public.department (department_id, name, head) VALUES ('FE1', 'Front End', 'ed');
INSERT INTO public.department (department_id, name, head) VALUES ('HR1', 'Human Resource', 'ysj');


--
-- TOC entry 2192 (class 0 OID 16404)
-- Dependencies: 183
-- Data for Name: employee; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.employee (employee_id, name, department, role) VALUES ('ysj', 'Yi Shi Jie', 'HR1', 'HRM1');
INSERT INTO public.employee (employee_id, name, department, role) VALUES ('ed', 'Er Duo', 'FE1', 'FEM1');
INSERT INTO public.employee (employee_id, name, department, role) VALUES ('sf', 'San Fran', 'BE1', 'BEM1');
INSERT INTO public.employee (employee_id, name, department, role) VALUES ('sf1', 'Sam Fasden', 'HR1', 'HRS1');
INSERT INTO public.employee (employee_id, name, department, role) VALUES ('cc', 'Charlie Charles', 'FE1', 'FES1');
INSERT INTO public.employee (employee_id, name, department, role) VALUES ('pif', 'Patrick Isaiah Filmore', 'BE1', 'BES1');


--
-- TOC entry 2193 (class 0 OID 16419)
-- Dependencies: 184
-- Data for Name: login_information; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.login_information (username, password, employee_id) VALUES ('yishijie', 'world123', 'ysj');
INSERT INTO public.login_information (username, password, employee_id) VALUES ('dazhu', 'julienne1', 'ed');
INSERT INTO public.login_information (username, password, employee_id) VALUES ('sanfran', 'sisco', 'sf');
INSERT INTO public.login_information (username, password, employee_id) VALUES ('sf1', 'password', 'sf1');
INSERT INTO public.login_information (username, password, employee_id) VALUES ('charleston', 'southcarolina', 'cc');
INSERT INTO public.login_information (username, password, employee_id) VALUES ('magicdragon', 'bythesea', 'pif');


--
-- TOC entry 2197 (class 0 OID 16470)
-- Dependencies: 188
-- Data for Name: rating_comment; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 2198 (class 0 OID 16483)
-- Dependencies: 189
-- Data for Name: rating_reply; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 2196 (class 0 OID 16444)
-- Dependencies: 187
-- Data for Name: rating_report; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 2191 (class 0 OID 16399)
-- Dependencies: 182
-- Data for Name: role; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.role (role_id, title, "isManager") VALUES ('HRS1', 'Human Resources Staff', false);
INSERT INTO public.role (role_id, title, "isManager") VALUES ('HRM1', 'Human Resources Manager', true);
INSERT INTO public.role (role_id, title, "isManager") VALUES ('FES1', 'Front End Staff', false);
INSERT INTO public.role (role_id, title, "isManager") VALUES ('FEM1', 'Front End Manager', true);
INSERT INTO public.role (role_id, title, "isManager") VALUES ('BES1', 'Back End Staff', false);
INSERT INTO public.role (role_id, title, "isManager") VALUES ('BEM1', 'Back End Manager', true);
INSERT INTO public.role (role_id, title, "isManager") VALUES ('SRM1', 'Senior Manager', true);


--
-- TOC entry 2194 (class 0 OID 16429)
-- Dependencies: 185
-- Data for Name: salary; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.salary (salary_id, wage, bonus) VALUES ('MS1', 150000, 20000);
INSERT INTO public.salary (salary_id, wage, bonus) VALUES ('SS1', 80000, 5000);
INSERT INTO public.salary (salary_id, wage, bonus) VALUES ('HP1', 20, 1);


--
-- TOC entry 2195 (class 0 OID 16434)
-- Dependencies: 186
-- Data for Name: work_day; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.work_day (day, employee_id, salary, hours) VALUES ('2018-01-01', 'ysj', 'MS1', -1);
INSERT INTO public.work_day (day, employee_id, salary, hours) VALUES ('2018-01-01', 'ed', 'MS1', -1);
INSERT INTO public.work_day (day, employee_id, salary, hours) VALUES ('2018-01-01', 'sf', 'MS1', -1);
INSERT INTO public.work_day (day, employee_id, salary, hours) VALUES ('2018-01-01', 'sf1', 'SS1', -1);
INSERT INTO public.work_day (day, employee_id, salary, hours) VALUES ('2018-01-01', 'cc', 'SS1', -1);
INSERT INTO public.work_day (day, employee_id, salary, hours) VALUES ('2018-01-02', 'pif', 'HP1', 8);
INSERT INTO public.work_day (day, employee_id, salary, hours) VALUES ('2018-01-03', 'pif', 'HP1', 8);
INSERT INTO public.work_day (day, employee_id, salary, hours) VALUES ('2018-01-04', 'pif', 'HP1', 8);
INSERT INTO public.work_day (day, employee_id, salary, hours) VALUES ('2018-01-05', 'pif', 'HP1', 8);


--
-- TOC entry 2051 (class 2606 OID 16398)
-- Name: department_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.department
    ADD CONSTRAINT department_pkey PRIMARY KEY (department_id);


--
-- TOC entry 2055 (class 2606 OID 16408)
-- Name: employee_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_pkey PRIMARY KEY (employee_id);


--
-- TOC entry 2057 (class 2606 OID 16423)
-- Name: login_information_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login_information
    ADD CONSTRAINT login_information_pkey PRIMARY KEY (username);


--
-- TOC entry 2065 (class 2606 OID 16477)
-- Name: rating_comment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rating_comment
    ADD CONSTRAINT rating_comment_pkey PRIMARY KEY (rating_comment_id);


--
-- TOC entry 2067 (class 2606 OID 16490)
-- Name: rating_reply_id; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rating_reply
    ADD CONSTRAINT rating_reply_id PRIMARY KEY (rating_reply_id);


--
-- TOC entry 2063 (class 2606 OID 16451)
-- Name: rating_report_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rating_report
    ADD CONSTRAINT rating_report_pkey PRIMARY KEY (rating_report_id);


--
-- TOC entry 2053 (class 2606 OID 16403)
-- Name: role_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.role
    ADD CONSTRAINT role_pkey PRIMARY KEY (role_id);


--
-- TOC entry 2059 (class 2606 OID 16433)
-- Name: salary_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.salary
    ADD CONSTRAINT salary_pkey PRIMARY KEY (salary_id);


--
-- TOC entry 2061 (class 2606 OID 16438)
-- Name: work_day_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.work_day
    ADD CONSTRAINT work_day_pkey PRIMARY KEY (day, employee_id);


--
-- TOC entry 2070 (class 2606 OID 16424)
-- Name: employee; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login_information
    ADD CONSTRAINT employee FOREIGN KEY (employee_id) REFERENCES public.employee(employee_id);


--
-- TOC entry 2068 (class 2606 OID 16409)
-- Name: employee_department; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_department FOREIGN KEY (department) REFERENCES public.department(department_id);


--
-- TOC entry 2069 (class 2606 OID 16414)
-- Name: employee_role; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_role FOREIGN KEY (role) REFERENCES public.role(role_id);


--
-- TOC entry 2075 (class 2606 OID 16491)
-- Name: rating_comment_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rating_reply
    ADD CONSTRAINT rating_comment_id FOREIGN KEY (rating_comment_id) REFERENCES public.rating_comment(rating_comment_id);


--
-- TOC entry 2074 (class 2606 OID 16478)
-- Name: rating_comment_report; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rating_comment
    ADD CONSTRAINT rating_comment_report FOREIGN KEY (rating_report_id) REFERENCES public.rating_report(rating_report_id);


--
-- TOC entry 2072 (class 2606 OID 16452)
-- Name: rating_report_reportee; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rating_report
    ADD CONSTRAINT rating_report_reportee FOREIGN KEY (reportee) REFERENCES public.employee(employee_id);


--
-- TOC entry 2073 (class 2606 OID 16457)
-- Name: rating_report_reporter; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rating_report
    ADD CONSTRAINT rating_report_reporter FOREIGN KEY (reporter) REFERENCES public.employee(employee_id);


--
-- TOC entry 2071 (class 2606 OID 16439)
-- Name: work_day_salary; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.work_day
    ADD CONSTRAINT work_day_salary FOREIGN KEY (salary) REFERENCES public.salary(salary_id);


--
-- TOC entry 2206 (class 0 OID 0)
-- Dependencies: 6
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2018-04-21 14:38:13 PDT

--
-- PostgreSQL database dump complete
--

