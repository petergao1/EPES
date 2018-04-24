--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.12
-- Dumped by pg_dump version 9.5.12

-- Started on 2018-04-24 08:14:12 PDT

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
-- TOC entry 2218 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 190 (class 1259 OID 32768)
-- Name: decision; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.decision (
    senior_manager character varying(16),
    dept_manager character varying(16),
    hr_staff character varying(16),
    decision text,
    decision_id character varying(16) NOT NULL
);


ALTER TABLE public.decision OWNER TO postgres;

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
    role character varying(16) NOT NULL,
    salary character varying(16)
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
    is_manager boolean NOT NULL
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
    hours double precision NOT NULL,
    approved boolean
);


ALTER TABLE public.work_day OWNER TO postgres;

--
-- TOC entry 2209 (class 0 OID 32768)
-- Dependencies: 190
-- Data for Name: decision; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.decision (senior_manager, dept_manager, hr_staff, decision, decision_id) FROM stdin;
sen	ed	sf1	Promotion:cc:To be promoted 2018-05-01	Promotionpif
\.


--
-- TOC entry 2200 (class 0 OID 16394)
-- Dependencies: 181
-- Data for Name: department; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.department (department_id, name, head) FROM stdin;
BE1	Back End	sf
FE1	Front End	ed
HR1	Human Resource	ysj
TEMPDEPT	Temporary 	\N
SR1	Senior Department	\N
\.


--
-- TOC entry 2202 (class 0 OID 16404)
-- Dependencies: 183
-- Data for Name: employee; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.employee (employee_id, name, department, role, salary) FROM stdin;
ed	Er Duo	FE1	FEM1	Manager1
pif	Patrick Isaiah Filmore	BE1	BES1	Staff1
sf	San Fran	BE1	BEM1	Manager1
sf1	Sam Fasden	HR1	HRS1	Staff1
ysj	Yi Shi Jie	HR1	HRM1	Manager1
stx	Stanley X	TEMPDEPT	TEMPROLE	TEMPSALARY
sen	Senior Banderas	SR1	SRM1	Manager1
cc	Charlie Charles	FE1	DES1	Staff1
\.


--
-- TOC entry 2203 (class 0 OID 16419)
-- Dependencies: 184
-- Data for Name: login_information; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.login_information (username, password, employee_id) FROM stdin;
yishijie	world123	ysj
dazhu	julienne1	ed
sanfran	sisco	sf
sf1	password	sf1
charleston	southcarolina	cc
magicdragon	bythesea	pif
stan	ley	stx
senior	banderas	sen
\.


--
-- TOC entry 2207 (class 0 OID 16470)
-- Dependencies: 188
-- Data for Name: rating_comment; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.rating_comment (rating_comment_id, comment, rating_report_id) FROM stdin;
18ysj0423sf1	Thanks Yi	2018-4-23sf1
\.


--
-- TOC entry 2208 (class 0 OID 16483)
-- Dependencies: 189
-- Data for Name: rating_reply; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.rating_reply (rating_reply_id, comment, rating_comment_id) FROM stdin;
\.


--
-- TOC entry 2206 (class 0 OID 16444)
-- Dependencies: 187
-- Data for Name: rating_report; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.rating_report (rating_report_id, report, reportee, reporter) FROM stdin;
2018-4-23sf1	Sam is good guy 5/5	sf1	ysj
18sf10423ed	Sam is decent guy 4/5	sf1	ed
\.


--
-- TOC entry 2201 (class 0 OID 16399)
-- Dependencies: 182
-- Data for Name: role; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.role (role_id, title, is_manager) FROM stdin;
HRS1	Human Resources Staff	f
HRM1	Human Resources Manager	t
FES1	Front End Staff	f
FEM1	Front End Manager	t
BES1	Back End Staff	f
BEM1	Back End Manager	t
SRM1	Senior Manager	t
TEMPROLE	Temporary Role	f
DEM1	Department Manager	t
DES1	Staff	f
\.


--
-- TOC entry 2204 (class 0 OID 16429)
-- Dependencies: 185
-- Data for Name: salary; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.salary (salary_id, wage, bonus) FROM stdin;
TEMPSALARY	0	0
Staff1	20	1
Manager1	150	20
SrManager1	80	5
\.


--
-- TOC entry 2205 (class 0 OID 16434)
-- Dependencies: 186
-- Data for Name: work_day; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.work_day (day, employee_id, hours, approved) FROM stdin;
2018-01-01	cc	8	\N
2018-01-01	sf	8	\N
2018-01-01	sf1	8	\N
2018-01-01	ysj	8	\N
2018-04-23	sf1	9	\N
2018-01-02	pif	8	\N
2018-01-03	pif	8	\N
2018-01-04	pif	8	\N
2018-01-05	pif	8	\N
2018-01-01	ed	6	t
\.


--
-- TOC entry 2074 (class 2606 OID 32775)
-- Name: decision_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.decision
    ADD CONSTRAINT decision_pkey PRIMARY KEY (decision_id);


--
-- TOC entry 2056 (class 2606 OID 16398)
-- Name: department_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.department
    ADD CONSTRAINT department_pkey PRIMARY KEY (department_id);


--
-- TOC entry 2060 (class 2606 OID 16408)
-- Name: employee_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_pkey PRIMARY KEY (employee_id);


--
-- TOC entry 2062 (class 2606 OID 16423)
-- Name: login_information_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login_information
    ADD CONSTRAINT login_information_pkey PRIMARY KEY (username);


--
-- TOC entry 2070 (class 2606 OID 16477)
-- Name: rating_comment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rating_comment
    ADD CONSTRAINT rating_comment_pkey PRIMARY KEY (rating_comment_id);


--
-- TOC entry 2072 (class 2606 OID 16490)
-- Name: rating_reply_id; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rating_reply
    ADD CONSTRAINT rating_reply_id PRIMARY KEY (rating_reply_id);


--
-- TOC entry 2068 (class 2606 OID 16451)
-- Name: rating_report_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rating_report
    ADD CONSTRAINT rating_report_pkey PRIMARY KEY (rating_report_id);


--
-- TOC entry 2058 (class 2606 OID 16403)
-- Name: role_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.role
    ADD CONSTRAINT role_pkey PRIMARY KEY (role_id);


--
-- TOC entry 2064 (class 2606 OID 16433)
-- Name: salary_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.salary
    ADD CONSTRAINT salary_pkey PRIMARY KEY (salary_id);


--
-- TOC entry 2066 (class 2606 OID 16438)
-- Name: work_day_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.work_day
    ADD CONSTRAINT work_day_pkey PRIMARY KEY (day, employee_id);


--
-- TOC entry 2084 (class 2606 OID 32781)
-- Name: decision_dept_manager; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.decision
    ADD CONSTRAINT decision_dept_manager FOREIGN KEY (dept_manager) REFERENCES public.employee(employee_id);


--
-- TOC entry 2085 (class 2606 OID 32786)
-- Name: decision_hr_staff; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.decision
    ADD CONSTRAINT decision_hr_staff FOREIGN KEY (hr_staff) REFERENCES public.employee(employee_id);


--
-- TOC entry 2083 (class 2606 OID 32776)
-- Name: decision_senior_manager; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.decision
    ADD CONSTRAINT decision_senior_manager FOREIGN KEY (senior_manager) REFERENCES public.employee(employee_id);


--
-- TOC entry 2078 (class 2606 OID 16424)
-- Name: employee; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login_information
    ADD CONSTRAINT employee FOREIGN KEY (employee_id) REFERENCES public.employee(employee_id);


--
-- TOC entry 2075 (class 2606 OID 16409)
-- Name: employee_department; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_department FOREIGN KEY (department) REFERENCES public.department(department_id);


--
-- TOC entry 2076 (class 2606 OID 16414)
-- Name: employee_role; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_role FOREIGN KEY (role) REFERENCES public.role(role_id);


--
-- TOC entry 2077 (class 2606 OID 24576)
-- Name: employee_salary; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_salary FOREIGN KEY (salary) REFERENCES public.salary(salary_id);


--
-- TOC entry 2082 (class 2606 OID 16491)
-- Name: rating_comment_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rating_reply
    ADD CONSTRAINT rating_comment_id FOREIGN KEY (rating_comment_id) REFERENCES public.rating_comment(rating_comment_id);


--
-- TOC entry 2081 (class 2606 OID 16478)
-- Name: rating_comment_report; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rating_comment
    ADD CONSTRAINT rating_comment_report FOREIGN KEY (rating_report_id) REFERENCES public.rating_report(rating_report_id);


--
-- TOC entry 2079 (class 2606 OID 16452)
-- Name: rating_report_reportee; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rating_report
    ADD CONSTRAINT rating_report_reportee FOREIGN KEY (reportee) REFERENCES public.employee(employee_id);


--
-- TOC entry 2080 (class 2606 OID 16457)
-- Name: rating_report_reporter; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rating_report
    ADD CONSTRAINT rating_report_reporter FOREIGN KEY (reporter) REFERENCES public.employee(employee_id);


--
-- TOC entry 2217 (class 0 OID 0)
-- Dependencies: 6
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2018-04-24 08:14:13 PDT

--
-- PostgreSQL database dump complete
--
