--
-- PostgreSQL database dump
--

-- Dumped from database version 16.4
-- Dumped by pg_dump version 16.4

-- Started on 2024-12-08 19:53:11

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 218 (class 1259 OID 16629)
-- Name: Charts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Charts" (
    in_spotify_charts integer NOT NULL,
    in_apple_charts integer NOT NULL,
    in_shazam_charts integer NOT NULL,
    track_id integer NOT NULL
);


ALTER TABLE public."Charts" OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16566)
-- Name: Favorite; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Favorite" (
    email character varying(255) NOT NULL,
    track_id integer NOT NULL
);


ALTER TABLE public."Favorite" OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16639)
-- Name: MusicalAttributes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."MusicalAttributes" (
    bpm integer NOT NULL,
    key character varying(255) NOT NULL,
    mode character varying(255) NOT NULL,
    "danceability_%" integer NOT NULL,
    "energy_%" integer NOT NULL,
    track_id integer NOT NULL
);


ALTER TABLE public."MusicalAttributes" OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16618)
-- Name: Track; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Track" (
    track_name character varying(255) NOT NULL,
    "artist(s)_name" character varying(255) NOT NULL,
    released_year integer,
    streams bigint,
    track_id integer
);


ALTER TABLE public."Track" OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 16559)
-- Name: User; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."User" (
    email character varying(255) NOT NULL,
    first_name character varying(255),
    last_name character varying(255)
);


ALTER TABLE public."User" OWNER TO postgres;

--
-- TOC entry 4712 (class 2606 OID 16633)
-- Name: Charts Charts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Charts"
    ADD CONSTRAINT "Charts_pkey" PRIMARY KEY (track_id, in_shazam_charts, in_apple_charts, in_spotify_charts);


--
-- TOC entry 4706 (class 2606 OID 16570)
-- Name: Favorite Favorite_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Favorite"
    ADD CONSTRAINT "Favorite_pkey" PRIMARY KEY (email, track_id);


--
-- TOC entry 4714 (class 2606 OID 16645)
-- Name: MusicalAttributes MusicalAttributes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."MusicalAttributes"
    ADD CONSTRAINT "MusicalAttributes_pkey" PRIMARY KEY (bpm, key, mode, "danceability_%", "energy_%", track_id);


--
-- TOC entry 4708 (class 2606 OID 16624)
-- Name: Track Track_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Track"
    ADD CONSTRAINT "Track_pkey" PRIMARY KEY (track_name, "artist(s)_name");


--
-- TOC entry 4704 (class 2606 OID 16565)
-- Name: User User_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."User"
    ADD CONSTRAINT "User_pkey" PRIMARY KEY (email);


--
-- TOC entry 4710 (class 2606 OID 16626)
-- Name: Track surrogate_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Track"
    ADD CONSTRAINT surrogate_key UNIQUE (track_id);


--
-- TOC entry 4715 (class 2606 OID 16571)
-- Name: Favorite User_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Favorite"
    ADD CONSTRAINT "User_fkey" FOREIGN KEY (email) REFERENCES public."User"(email);


--
-- TOC entry 4716 (class 2606 OID 16634)
-- Name: Charts track_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Charts"
    ADD CONSTRAINT track_fkey FOREIGN KEY (track_id) REFERENCES public."Track"(track_id);


--
-- TOC entry 4717 (class 2606 OID 16646)
-- Name: MusicalAttributes track_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."MusicalAttributes"
    ADD CONSTRAINT track_fkey FOREIGN KEY (track_id) REFERENCES public."Track"(track_id);


-- Completed on 2024-12-08 19:53:11

--
-- PostgreSQL database dump complete
--

