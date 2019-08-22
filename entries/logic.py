from entries.models import entry_data_new, configdata, gw_results

#score update
class processgwresult:
    def run(self, gw):
        current_gw = gw
        gw_entries = entry_data_new.objects.filter(entry_gw_id__pk = current_gw)
        gw_res = gw_results.objects.get(entry_gw__pk = current_gw)
        for entry in gw_entries:
            homescore1 = entry.score_home_fid1
            awayscore1 = entry.score_away_fid1
            reshome1 = gw_res.score_home_fid1
            resaway1 = gw_res.score_home_fid2
            entry_res = processgwresult.matchscore(homescore1, awayscore1)
            actual_res = processgwresult.matchscore(reshome1, resaway1)
            print (homescore1, awayscore1, reshome1, resaway1, entry_res, actual_res)
            if entry_res == actual_res:
                match_entry_score = entry_res
            else:
                match_entry_score = 0
            if homescore1 == reshome1 and awayscore1 == resaway1:
                if homescore1 + awayscore1 > 4:
                    score_bonus  = 5
                else:
                    score_bonus = 7
            else:
                score_bonus = 0
            gamerese  = score_bonus + match_entry_score
        return gamerese

    def matchscore(homescore, awayscore):
        if homescore > awayscore:
            game_result = 3
        elif awayscore > homescore:
            game_result  = 5
        elif homescore == awayscore:
            game_result  = 4
        else:
            game_result = 0
        return game_result
