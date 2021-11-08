package com.cybergames.repository

import com.cybergames.entities.*
import org.springframework.data.repository.CrudRepository

interface TeamRepository : CrudRepository<Team, Long>
interface UserRepository : CrudRepository<User, Long>
interface TournamentRepository : CrudRepository<Tournament, Long>
interface GenreRepository : CrudRepository<Genre, Long>
interface GameRepository : CrudRepository<Game, Long>
